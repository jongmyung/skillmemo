from memo.models import Users, Memos, DMs
from memo.tabs import *
from memo.ownerInfo import *

class crumbSearch:
    def __init__(self, user_id, crumb, session):
        self.account_owner = Users.objects.get(user_id=user_id)
        self.ownerInfo = Owner(user_id)
        self.keyword = crumb
        self.session = session
        self.owner_memos_public = Memos.objects.filter(made_by=self.account_owner, disclose="public").exclude(tab_name="TRASH")
        self.owner_memos = Memos.objects.filter(made_by=self.account_owner).exclude(tab_name="TRASH")
        if self.session:
            self.logged_user = Tabs(self.session)
            if self.account_owner.user_id != self.session:
                self.memos_found = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword, disclose="public" ).exclude(tab_name="TRASH")
                dms_got = DMs.objects.filter(to=self.logged_user.user)
                dms_got_nocheck = DMs.objects.filter(to=self.logged_user.user, if_to_checked="no")
                dms_got_noReplyCheck = DMs.objects.filter(to=self.logged_user.user, if_to_reply_checked="no")
                dms_sent = DMs.objects.filter(sent_by=self.logged_user.user)
                dms_sent_noReplyCheck = DMs.objects.filter(sent_by=self.logged_user.user, if_from_reply_checked="no")
                dms_notificaion_count = len(dms_got_nocheck) + len(dms_got_noReplyCheck) + len(dms_sent_noReplyCheck)
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
                    'category':"keyword",
                    'dms_got':dms_got,
                    'dms_got_nocheck':dms_got_nocheck,
                    'dms_got_noReplyCheck':dms_got_noReplyCheck,
                    'dms_sent':dms_sent,
                    'dms_sent_noReplyCheck':dms_sent_noReplyCheck,
                    'dms_notification_count': dms_notificaion_count,
                }
            else:
                self.memos_found = Memos.objects.filter(made_by=self.account_owner, keyword__icontains=self.keyword).exclude(tab_name="TRASH")
                dms_got = DMs.objects.filter(to=self.account_owner)
                dms_got_nocheck = DMs.objects.filter(to=self.account_owner, if_to_checked="no")
                dms_got_noReplyCheck = DMs.objects.filter(to=self.account_owner, if_to_reply_checked="no")
                dms_sent = DMs.objects.filter(sent_by=self.account_owner)
                dms_sent_noReplyCheck = DMs.objects.filter(sent_by=self.account_owner, if_from_reply_checked="no")
                dms_notificaion_count = len(dms_got_nocheck) + len(dms_got_noReplyCheck) + len(dms_sent_noReplyCheck)
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
                    'category':"keyword",
                    'dms_got':dms_got,
                    'dms_got_nocheck':dms_got_nocheck,
                    'dms_got_noReplyCheck':dms_got_noReplyCheck,
                    'dms_sent':dms_sent,
                    'dms_sent_noReplyCheck':dms_sent_noReplyCheck,
                    'dms_notification_count': dms_notificaion_count,
                }
        else:
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