import praw, re, random, os

r = praw.Reddit("A bot to send butt tips to users by /u/Natatos")
r.login(os.environ["USERNAME"], os.environ["PASSWORD"])
if r.is_logged_in():
  print "Logged in"
else:
  print "Problem logging in"
  exit()

def choose_reply():
  with open("replies.txt") as f:
    replies = f.readlines()
  return random.choice(replies)

def reply_to_comment(comment):
  values = {
    "to": comment.body.split()[-1],
    "amount": comment.body.split()[0]
  }
  reply = "Sending {0} ButtTips to {1}\n\n{2}".format(values["amount"], values["to"], choose_reply())
  comment.reply(reply)

for comment in praw.helpers.comment_stream(r, "enoughlibrarianspam"):
  if re.search("\+[.0-9]* (ButtTip to [/u])", comment.body, re.IGNORECASE):
    reply_to_comment(comment)
