# zlp
A command line interface for zulip. 

# Documentation 
##zulip email=youremail
 Set your Zulip account's email address.
 
#zulip api=yourkey
 Set your Zulip account's API key.

zulip filter=default args 
 Save a filter with name "default". You cannot name a filter zulip, d, h, stream, private, tagged or msg.
  stream
  ------
    If stream=foo, filtered content will only show only messages in the stream foo.
  private
  ---
    If private=true, filtered content will only show only private messages. If private=false or omitted, no filter is applied.
  --
  tagged
    If tagged=true, filtered content will only show only messages in which you are tagged. If tagged=false or omitted, no filter is applied.

#zulip news args
 Show all posts since the last time you ran zulip news (or if you have never used the news command before, show all posts since you first provided your API key to zlp.)
 ## stream
    If stream=foo, show only messages in the stream foo.
 ## private
    If private=true, show only private messages. If private=false or omitted, show all messages.
  tagged
    If tagged=true, show only messages in which you are tagged. If tagged=false or omitted, show all messages.
  filter
    Apply a saved filter. See the "zulip filter" documentation. The word filter can be omitted (zulip news py and zulip news filter="py" are equivalent).

zulip msg args "content"
 send a message. you must provide either a stream or users.
  stream
    If stream=foo, your message will be posted to the stream "foo"
  users
    Use either users=ex@mail.com or users=[ex@mail.com,ex2@mail.com,ex3@mail.com] for multiple recipients. 
    
zulip hist args
  d
    Show the last n days of messages. For example, zulip hist d=2 shows the last 2 days of messages.
  h
    Show the last n hours of messages. For example, zulip hist h=2 shows the last 2 hours of messages.
  stream
    If stream=foo, show only messages in the stream foo.
  private
    If private=true, show only private messages. If private=false or omitted, show all messages.
  tagged
    If tagged=true, show only messages in which you are tagged. If tagged=false or omitted, show all messages.
  filter
    Apply a saved filter. See the "zulip filter" documentation. The word filter can be omitted (zulip news py and zulip news filter="py" are equivalent).