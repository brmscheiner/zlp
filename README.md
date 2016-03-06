# zlp
zlp is a command line interface for zulip. 

## Installation 
Ask your computer politely to install zlp.

## okay, how do I use it? 
######zulip set_email=youremail
> Set your Zulip account's email address.
 
######zulip set_api=yourkey
> Set your Zulip account's API key. To get your API key, go to zulip.com -> settings -> show/change API key.

######zulip filter=foo args 
> Save a filter with name foo. You cannot name a filter zulip, d, h, stream, private, tagged or msg. Optional arguments:
* stream: If stream=foo, filtered content will only show only messages in the stream foo.
* private: If private=true, filtered content will only show only private messages. If private=false or omitted, no filter is applied.
* tagged: If tagged=true, filtered content will only show only messages in which you are tagged. If tagged=false or omitted, no filter is applied.

######zulip news args
> Show all posts since the last time you ran zulip news (or if you have never used the news command before, show all posts since you first provided your API key to zlp). Optional arguments:
 * stream: If stream=foo, show only messages in the stream foo.
 * private: If private=true, show only private messages. If private=false or omitted, show all messages.
 * **tagged:** If tagged=true, show only messages in which you are tagged. If tagged=false or omitted, show all messages.
 * filter: Apply a saved filter. See the "zulip filter" documentation. The word filter can be omitted (zulip news py and zulip news filter="py" are equivalent).

######zulip hist args
> Show posts from the last _x_ days or hours. Either d or h must be supplied.
*d: Show the last n days of messages. For example, zulip hist d=2 shows the last 2 days of messages.
*h: Show the last n hours of messages. For example, zulip hist h=2 shows the last 2 hours of messages.
*stream: If stream=foo, show only messages in the stream foo.
*private: If private=true, show only private messages. If private=false or omitted, show all messages.
*tagged: If tagged=true, show only messages in which you are tagged. If tagged=false or omitted, show all messages.
*filter: Apply a saved filter. See the "zulip filter" documentation. The word filter can be omitted (zulip news py and zulip news filter="py" are equivalent).

######zulip msg args "content"
> send a message. you must provide either a stream or users.
*stream: If stream=foo, your message will be posted to the stream "foo"
*users: Use either users=ex@mail.com or users=[ex@mail.com,ex2@mail.com,ex3@mail.com] for multiple recipients. 

