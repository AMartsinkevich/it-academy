from rest_framework import serializers


# Fields ------------------------------

class ContractSerializer(serializers.Serializer):

    ba_id = serializers.IntegerField()
    cs_id = serializers.IntegerField()
    co_id = serializers.IntegerField()
    co_id_pub = serializers.CharField()


class SaleResponseSerializer(serializers.Serializer):

    date = serializers.DateField()


# Request ------------------------------
{
    "type_sale": 4800,
    "contract": {
        "ba_id": 9831714,
        "cs_id": 6275283,
        "co_id": 17484544,
        "co_id_pub": "000020011088458"
    }
}

class SalesRequestSerializer(serializers.Serializer):

    type_sale = serializers.IntegerField()
    contract = ContractSerializer()


# Response ------------------------------
{
    "status": "OK",
    "contract": {
        "ba_id": 9831714,
        "cs_id": 6275283,
        "co_id": 17484544,
        "co_id_pub": "000020011088458"
    },
    "xml": "<?xml version='1.0'?><input_params>...</input_params>",
    "sale": {
        "date": "2025-06-06"
    }
}

class SalesResponseSerializer(serializers.Serializer):
    
    status = serializers.CharField()
    contract = ContractSerializer()
    xml = serializers.CharField()
    sale = SaleResponseSerializer()
