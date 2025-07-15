from django.db.models.fields import return_None
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaulttags import comment
from properties.models import Property, DealRequest
from properties.forms import DealRequestForm, PropertyForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.

def properties_list(request):
    properties = Property.objects.filter(available=True)

    return render(request, template_name='properties_list.html',
    # return render(request, template_name='main/catalog.html',
                  context={'properties': properties})


def property_detail(request, prop_id):
    prop_obj = get_object_or_404(Property, id=prop_id)
    # prop_obj = Property.objects.filter(id=prop_id)
    # prop_obj = Property.objects.get(id=prop_id)

    return render(request, template_name='property_detail.html',
                  context={'property': prop_obj})

@login_required
def create_deal_request(request, prop_id):
    property_obj = get_object_or_404(Property, id=prop_id)

    if request.method == 'POST':
        form = DealRequestForm(request.POST)

        if form.is_valid():
            deal_request = form.save(commit=False)
            deal_request.seeker = request.user
            deal_request.property = property_obj
            deal_request.save()
            return redirect('properties:detail', prop_id=prop_id)
    else:
        form = DealRequestForm()

    return render(request, template_name='deal_request_form.html', context={'form': form, 'property': property_obj})

@login_required()
def owner_requests_list(request):
    deal_requests = (
        DealRequest.objects
            .select_related('property', 'seeker')
            .filter(property__owner=request.user)
            .order_by('-created_at')
    )
    return render(request, template_name='owner_requests.html', context={'deal_requests': deal_requests})

@login_required()
def seeker_requests_list(request):
    deal_requests = (
        DealRequest.objects
            .select_related('property')
            .filter(seeker=request.user)
            .order_by('-created_at')
    )
    print(deal_requests)
    return render(request, template_name='seeker_requests.html', context={'deal_requests': deal_requests})

@login_required
@require_POST
def approve_request(request, deal_request_id):
    deal = get_object_or_404(
        DealRequest,
        id=deal_request_id,
        property__owner=request.user,
        status=DealRequest.STATUSES[0][0]
    )
    deal.status = DealRequest.STATUSES[1][0]
    deal.save()

    deal.property.available = False
    deal.property.save(update_fields=['available'])
    return redirect('properties:owner_requests')

@login_required
@require_POST
def reject_request(request, deal_request_id):
    deal = get_object_or_404(
        DealRequest,
        id=deal_request_id,
        property__owner=request.user,
        status=DealRequest.STATUSES[0][0]
    )
    deal.status = DealRequest.STATUSES[2][0]
    deal.save()

    return redirect('properties:owner_requests')


@login_required
def create_property(request):
    if not request.user.is_owner():
        return redirect('properties:list')
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.owner = request.user
            property_obj.save()
            return redirect('properties:detail', prop_id=property_obj.pk)
    else:
        form = PropertyForm()

    return render(request, template_name='property_form.html', context={'form': form})

@login_required
def edit_property(request, prop_id):
    if not request.user.is_owner():
        return redirect('properties:list')

    property_obj = get_object_or_404(Property, pk=prop_id, owner=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            property_obj.save()
            return redirect('properties:detail', prop_id=property_obj.pk)
    else:
        form = PropertyForm(instance=property_obj)

    return render(request, template_name='property_form.html', context={'form': form})
