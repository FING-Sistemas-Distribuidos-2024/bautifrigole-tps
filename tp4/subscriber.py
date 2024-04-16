import zmq

connect_to = "tcp://localhost:3000"
topic_to_subscribe = b'sd are fun!'

def main() -> None:
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)
    s.setsockopt(zmq.SUBSCRIBE, topic_to_subscribe)

    print(f"Subscribed to topic: {topic_to_subscribe.decode('utf8')}")

    try:
        while True:
            topic, msg_body = s.recv_multipart()
            print(f"Received message: Topic: {topic.decode('utf8')}, Message: {msg_body.decode('utf8')}")
    except KeyboardInterrupt:
        pass

    print("Done.")

if __name__ == "__main__":
    main()
