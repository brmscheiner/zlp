#zlp
zlp is a command line interface for [Zulip](https://zulip.com/). 

##Installation 
zlp is currently under development! 

##Usage
`zulip set_email youremail` sets your Zulip account's email address. The email address and API key must be set before zlp can function properly -- this is the equivalent to logging in to Zulip.
 
`zulip set_api yourkey` sets your Zulip account's API key. To get your API key, go to zulip.com -> settings -> show/change API key.

`zulip filter=foo args` saves a filter with name foo. You cannot name a filter zulip, d, h, stream, private, tagged or msg. There are three optional arguments:
* stream: If stream=foo, filtered content will only show only messages in the stream foo.
* private: If private=true, filtered content will only show only private messages. If private=false or omitted, no filter is applied.
* tagged: If tagged=true, filtered content will only show only messages in which you are tagged. If tagged=false or omitted, no filter is applied.

`zulip news args` shows all posts since the last time you ran zulip news (or if you have never used the news command before, show all posts since you first provided your API key to zlp). Optional arguments:
 * stream: If stream=foo, show only messages in the stream foo.
 * private: If private=true, show only private messages. If private=false or omitted, show all messages.
 * tagged: If tagged=true, show only messages in which you are tagged. If tagged=false or omitted, show all messages.
 * filter: Apply a saved filter. See the "zulip filter" documentation. The word filter can be omitted (zulip news py and zulip news filter="py" are equivalent).

`zulip hist args` shows posts from the last _x_ days or hours. Either d or h must be supplied.
* d: Show the last n days of messages. For example, zulip hist d=2 shows the last 2 days of messages.
* h: Show the last n hours of messages. For example, zulip hist h=2 shows the last 2 hours of messages.
* stream: If stream=foo, show only messages in the stream foo.
* private: If private=true, show only private messages. If private=false or omitted, show all messages.
* tagged: If tagged=true, show only messages in which you are tagged. If tagged=false or omitted, show all messages.
* filter: Apply a saved filter. See the "zulip filter" documentation. The word filter can be omitted (zulip news py and zulip news filter="py" are equivalent).

`zulip msg args "content"` sends a message. You must provide either a stream or users. If stream is supplied, you must supply a subject as well.
* stream: If stream=foo, your message will be posted to the stream "foo"
* subject: Use this argument only if you are posting a message to a stream. Private messages in Zulip do not have subjects.
* to: Use either users=ex@mail.com or to=[ex@mail.com,ex2@mail.com,ex3@mail.com] for multiple recipients. 

