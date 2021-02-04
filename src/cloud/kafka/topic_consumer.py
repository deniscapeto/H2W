from kafka import KafkaConsumer

def read_all_messages():
    """
    LER TODAS AS MENSAGENS
    """
    consumer = KafkaConsumer(
        'teste_kefka_python',
        auto_offset_reset='earliest',
        enable_auto_commit=False
    )
    for msg in consumer:
        print (msg)


def listen_to_new_messages():
    consumer = KafkaConsumer(
        'teste_kefka_python'
    )
    for msg in consumer:
        print (msg)

read_all_messages()