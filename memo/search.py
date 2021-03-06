from memo.models import Users, Memos
from memo.tabs import *
from memo.ownerInfo import *
class Search:
    def __init__(self, user_id, search_keyword, session):
        self.account_owner = Users.objects.get(user_id=user_id)
        self.ownerInfo = Owner(user_id)
        self.keyword = search_keyword
        self.session = session
        self.owner_memos_public = Memos.objects.filter(made_by=self.account_owner, disclose="public").exclude(tab_name="TRASH")
        self.owner_memos = Memos.objects.filter(made_by=self.account_owner)
        self.logged_user = ""
        if self.session:            
            self.logged_user = Tabs(self.session)
            if self.keyword[0] == "!":
                self.keyword = self.keyword[1:]
                if self.account_owner.user_id != self.session: #for logged user context with ! keyword search
                    self.memos_found = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword, disclose="public" ).exclude(tab_name="TRASH")
                    self.context = {
                        'keyword':self.keyword,
                        'memos_found':self.memos_found,
                        'account_owner':self.account_owner,
                        'logged_user':self.logged_user.user,
                        'account_owner_memos': self.owner_memos_public,
                        'account_owner_memos_count':self.owner_memos_public.count,
                        'crumbs': self.ownerInfo.PublicCrumbs,
                        'tab01':self.logged_user.tab01,
                        'tab02':self.logged_user.tab02,
                        'tab03':self.logged_user.tab03,
                        'tab04':self.logged_user.tab04,
                        'tab05':self.logged_user.tab05,
                        'category':"keyword"
                    }
                else: #for owner context with ! keyword search
                    self.memos_found = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword)
                    self.context = {
                        'keyword':self.keyword,
                        'memos_found':self.memos_found,
                        'account_owner':self.account_owner,
                        'logged_user':self.logged_user.user,
                        'account_owner_memos': self.owner_memos,
                        'account_owner_memos_count':self.owner_memos.count,
                        'crumbs': self.ownerInfo.Crumbs,
                        'tab01':self.logged_user.tab01,
                        'tab02':self.logged_user.tab02,
                        'tab03':self.logged_user.tab03,
                        'tab04':self.logged_user.tab04,
                        'tab05':self.logged_user.tab05,
                        'category':"keyword"
                    }
            else:
                if self.account_owner.user_id != session: # for logged user context with subject search
                    self.memos_found = Memos.objects.filter(made_by=self.account_owner, subject__icontains=self.keyword, disclose="public" ).exclude(tab_name="TRASH")
                    self.context = {
                        'keyword':self.keyword,
                        'memos_found':self.memos_found,
                        'account_owner':self.account_owner,
                        'logged_user':self.logged_user.user,
                        'account_owner_memos': self.owner_memos_public,
                        'account_owner_memos_count':self.owner_memos_public.count,
                        'crumbs': self.ownerInfo.PublicCrumbs,
                        'tab01':self.logged_user.tab01,
                        'tab02':self.logged_user.tab02,
                        'tab03':self.logged_user.tab03,
                        'tab04':self.logged_user.tab04,
                        'tab05':self.logged_user.tab05,
                        'category':"subject"
                    }
                else: # owner context with subject search
                    self.memos_found = Memos.objects.filter(made_by=self.account_owner, subject__icontains=self.keyword)
                    self.context = {
                        'keyword':self.keyword,
                        'memos_found':self.memos_found,
                        'account_owner':self.account_owner,
                        'logged_user':self.logged_user.user,
                        'account_owner_memos': self.owner_memos,
                        'account_owner_memos_count':self.owner_memos.count,
                        'crumbs': self.ownerInfo.Crumbs,
                        'tab01':self.logged_user.tab01,
                        'tab02':self.logged_user.tab02,
                        'tab03':self.logged_user.tab03,
                        'tab04':self.logged_user.tab04,
                        'tab05':self.logged_user.tab05,
                        'category':"subject"
                    }
        else:
            if self.keyword[0] == "!":
                self.keyword = self.keyword[1:]
                self.memos_found = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword, disclose="public" ).exclude(tab_name="TRASH")
                self.context = {
                    'keyword':self.keyword,
                    'memos_found':self.memos_found,
                    'account_owner':self.account_owner,
                    'account_owner_memos': self.owner_memos_public,
                    'account_owner_memos_count':self.owner_memos_public.count,
                    'crumbs': self.ownerInfo.PublicCrumbs,
                    'category':"keyword"
                }
            else:
                self.memos_found = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword)
                self.context = {
                    'keyword':self.keyword,
                    'memos_found':self.memos_found,
                    'account_owner':self.account_owner,
                    'account_owner_memos': self.owner_memos,
                    'account_owner_memos_count':self.owner_memos.count,
                    'crumbs': self.ownerInfo.Crumbs,
                    'category':"keyword"
                }