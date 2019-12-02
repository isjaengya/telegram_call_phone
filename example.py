import pyrogram
from tgvoip import VoIPServerConfig
from tgvoip_pyrogram import VoIPFileStreamService


def telegram_init_session():
    VoIPServerConfig.set_bitrate_config(80000, 100000, 60000, 5000, 5000)
    client = pyrogram.Client('session_name', api_id=1111111, api_hash='d969f84xxxxxxxxxxxxxxxxxxxxxxxxx')
    # client = pyrogram.Client('session_name', api_id=, api_hash='')
    client.start()

    voip_service = VoIPFileStreamService(client, receive_calls=False)
    call = voip_service.start_call('@xxxx')  # 这里填写用户名
    call.play('input.raw')  # 要输入的音频文件
    call.play_on_hold(['input.raw'])
    # call.set_output_file('output.raw')  # 这里是用户语音内容保存的文件, 你呼叫的用户的内容

    @call.on_call_state_changed
    def state_changed(call, state):
        print('State changed:', call, state)

    # you can use `call.on_call_ended(lambda _: app.stop())` here instead
    @call.on_call_ended
    def call_ended(call):
        client.stop()


if __name__ == '__main__':
    telegram_init_session()
