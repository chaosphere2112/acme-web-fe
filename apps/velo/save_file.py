import VeloAPI
import os
import sys


def save_file(text, filename, site_user, velo_username, password):

    velo_api = VeloAPI.Velo()
    if not velo_api.isJVMStarted():
        velo_api.start_jvm()
    rs = velo_api.init_velo(velo_username, password)

    local_path = os.getcwd() + '/userdata/' + velo_username + '/'
    try:
        f = open(local_path + filename, 'w')
        f.write(text)
        f.close()
    except:
        print 'I/O failure when writing file to django server'

    if velo_api.upload_file(local_path, filename) >= 0:
        print 'File saved'
        return 0
    else:
        print 'Error saving file', local_path, filename
        return -1


exit_code = save_file(text=sys.argv[1], filename=sys.argv[2], site_user=sys.argv[3],
                      velo_username=sys.argv[4], password=sys.argv[5])

sys.exit(exit_code)
