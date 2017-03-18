""" The class containing infomation about a commit group's user """
class CommitMember():
    member_count = 0 # For counting whole member
    def __init__(self, input_username='', input_repos=[], input_committed=False):
        CommitMember.member_count += 1
        self.__username = input_username
        self.__repos = input_repos
        self.__committed = input_committed

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, input_username):
        self.__username = input_username

    @property
    def repos(self):
        return self.__repos

    @repos.setter
    def repos(self, input_repos):
        self.__repos = input_repos

    @property
    def committed(self):
        return self.__committed

    @committed.setter
    def committed(self, input_committed):
        self.__committed = input_committed

    @staticmethod
    def total_members(): # staticmethod does not need either parameter 'cls' or 'self'
        return CommitMember.member_count
    """
    @classmethod
    def total_members(cls): # classmethod needs the parameter 'cls'
        return CommitMember.member_count
    """
   
    def __repr__(self):
        """For example: >> obj """
        return "CommitMember('" + self.__username + "')"

    def __str__(self):
        """For example: >> print(obj) """
        return "username: %s / repos: %s / committed: %s" %(self.__username, self.__repos, self.__committed)

