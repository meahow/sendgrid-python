prism 2.x downsides
- 30% slower
- validate does not work properly with sendgrid
  - 502 bad gateway on a hello world sendgrid example
  - can't do SSL, at least not in docker, no documentation how to do this
  - it does work for basic GET and for petstore swagger example
- closed source
- insufficient and outdated docs
- beforeScript seems to to stopped working
- validate passes requests to the same scheme as it gets (http vs https) and because https is not functional it requires OAI change

prims 2.x upsides
- it detected a bu in the tests (200 returned instead of 400 for not-existant endpoint) 

prism downsides
- can't do SSL, at least not in docker, no documentation how to do this
- closed source
- insufficient and outdated docs
- hard to troublleshoot/debug as there is no way to log the whole request coming in
  - in 0.6 the logged request was empty (no headers, no data)
  - in 2.0 the scripting is not working at all
- separate oai spec necessary for prism ?