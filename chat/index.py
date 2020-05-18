import pusher

pusher_client = pusher.Pusher(
  app_id='1003163',
  key='8c79ce334c02dce24cf0',
  secret='54a04ba02786bb6971c6',
  cluster='ap3',
  ssl=True
)

pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})