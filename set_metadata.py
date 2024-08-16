
from substrateinterface import SubstrateInterface, Keypair
import os

wsendpoint = os.getenv("WSENDPOINT")
collectionid = os.getenv("COLLECTIONID")


def set_metadata(item_id, cid):
    substrate = SubstrateInterface(url=wsendpoint)

    keypair = Keypair.create_from_uri(os.getenv("METADATASECRETKEY"))

    call = substrate.compose_call(call_module="Nfts", call_function="set_metadata", call_params={
        "collection": collectionid,
        "item": item_id,
        "data": f"ipfs://{cid}"
    })

    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair, era={'period': 64})

    try:
        receipt = substrate.submit_extrinsic(extrinsic)
    except:
        print("failed :(")
