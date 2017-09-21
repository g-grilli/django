from fabric.api import run, env, sudo, cd, prefix

env.hosts = ['108.61.241.147']
env.user = 'ggril'

DIR = '/home/ggril/Django_exercise'
VENV = 'source /home/ggril/.virtualenvs/website/bin/activate && source SECRETS.ENV'

def start ():
  with cd(DIR):
    with prefix(VENV):
      run('pm2 start uwsgi -- --ini uwsgi.ini > start.log')
      
def stop ():
  run('pm2 stop all > stop.log')
  
def deploy ():
  with cd(DIR):
    run('git pull')
    
    with prefix(VENV):
      run('pip install -r requirements.txt  > install.log')
      
    run('pm2 restart all > restart.log')
    
def hello ():
  print("Hello")