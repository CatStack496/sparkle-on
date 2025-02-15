[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fvercel%2Fexamples%2Ftree%2Fmain%2Fpython%2Fflask3&demo-title=Flask%203%20%2B%20Vercel&demo-description=Use%20Flask%203%20on%20Vercel%20with%20Serverless%20Functions%20using%20the%20Python%20Runtime.&demo-url=https%3A%2F%2Fflask3-python-template.vercel.app%2F&demo-image=https://assets.vercel.com/image/upload/v1669994156/random/flask.png)

# Sparkle-on

I built this little Python Flask webserver to act image server for things like Slack or Discord so it would embed an image instead of a link. I built this app as a joke for my friends and I so I could send them a "sparkle on", a strange gif of Jerma985 with his hand on his hip with sparkling text in front of him that normally says "Sparkle on; it's Wednesday; dont forget to be yourself", of the current eastern time day. Alas, despite setting the headers correctly on flask, Discord ignores headers and caches images anyways, so if this site had been used in a certain amount of time before resending it, it could cause a different outcome for different people and often be incorrect.

## Try it yourself!

https://sparkle-on/vercel.app/
