from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'https://jenkins.flodev.net'
    server = Jenkins(jenkins_url, username='admin', password='Nghial@1')
    return server

if __name__ == '__main__':
    print get_server_instance().version
    # print 
