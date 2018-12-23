class Request:
    __slots__ = ['object_kind', 'event_name', 'user_name', 'user_username', 'project', 'repository', 'homepage',
                 'commits']

    def __init__(self, data):
        self.object_kind = data.get('object_kind')
        self.event_name = data.get('event_name')
        self.user_name = data.get('user_name')
        self.user_username = data.get('user_username')
        self.project = data.get('project')
        self.repository = data.get('repository')
        self.homepage = data.get('homepage')
        self.commits = data.get('commits')
