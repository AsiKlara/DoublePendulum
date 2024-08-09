from substrateinterface import SubstrateInterface

ws_endpoint = "wss://rococo-asset-hub-rpc.polkadot.io"
collection_id = 314

sender = "5DAM8XCuWwxkh42NFBXaAnH6v7jYbd3uQjVKkLPre5LTtmTL"
api = SubstrateInterface(url=ws_endpoint)

# Get collection info
collection = api.query('Nfts', 'Collection', [collection_id])

# Get the new item ID (assuming it is stored in the collection's "items" field)
new_item_id = collection.value['items']

print(f"new itemId: {new_item_id}")


call = api.compose_call(
    call_module='Nfts',
    call_function='mint',
    call_params={
        'collection_id': collection_id,
        'item_id': new_item_id,
        'owner': sender,
        'witness_data': None
    }
)

print(call)

'''extrinsic = api.create_signed_extrinsic(call=call, keypair=sender_keypair)
receipt = api.submit_extrinsic(extrinsic, wait_for_inclusion=True)

print(f"Extrinsic '{receipt.extrinsic_hash}' sent and included in block '{receipt.block_hash}'")
except SubstrateRequestException as e:
print(f"Failed to send: {e}")'''


