from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMIN")
IP = env.str("IP")


# test