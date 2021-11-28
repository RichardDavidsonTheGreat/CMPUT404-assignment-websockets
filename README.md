CMPUT404-assignment-websockets
==============================

CMPUT404-assignment-websockets

See requirements.org (plain-text) for a description of the project.

Make a shared state Websockets drawing program

Prereqs
=======
Create a virtual environment and install the required dependencies.

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements.txt
```

Contributors / Licensing
========================

Generally everything is LICENSE'D under the Apache 2 license by Abram Hindle.

freetests.py is LICENSE'D under a BSD-like license:

From ws4py

Copyright (c) 2011-2014, Sylvain Hellegouarch, Abram Hindle
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
 * Neither the name of ws4py nor the names of its contributors may be used
   to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Davidson, Richard 2021

I (Richard Davidson 1501248) used the following ressources in completeing this assignment Information and much of the code responsible for the use of requests with promises is not mine and was taken from the CMPUT404 class notes In particular CMPUT 404 Web Applications and Architecture Part 08: AJAX Created by Abram Hindle (abram.hindle@ualberta.ca) and Hazel Campbell (hazel.campbell@ualberta.ca). Copyright 2014-2019. https://uofa-cmput404.github.io/cmput404-slides/08-AJAX.html#/4 - https://uofa-cmput404.github.io/cmput404-slides/08-AJAX.html#/10

Information and much of the code responsible for the use of websockets and implementing the listener pattern with websockets is not mine and was taken from the CMPUT404 class github repository in particular https://github.com/uofa-cmput404/cmput404-slides/blob/master/examples/WebSocketsExamples/chat.py and https://github.com/uofa-cmput404/cmput404-slides/blob/master/examples/WebSocketsExamples/static/chat.html

I also used the following online ressources:

https://developer.mozilla.org/en-US/docs/Web/API/Request for information on creating and sending different types of requests with Fetch

https://stackoverflow.com/questions/4162749/convert-js-object-to-json-string answer by Andris on how to use JSON.stringify() to convert to JSON

https://www.javascripttutorial.net/web-apis/javascript-arc/ for knowledge on javascript and in particular use of canvas for infomation on how to fill objects

https://www.colorhexa.com/ff8c00 for css colour codes #ff4c00 #ffb700

https://clrs.cc/ for css colour Maroon

https://html-color.codes/purple for css colours darkslateblue and rebeccapurple

https://html-color.codes/green for css colour darkgreen

https://www.w3schools.com/python/python_try_except.asp for knowledge on using try catch blocks in python

https://stackoverflow.com/questions/7824101/return-http-status-code-201-in-flask answer by Iacks showed me how to return a body and status code in Flask

https://stackoverflow.com/questions/12435297/how-do-i-jsonify-a-list-in-flask answer by FogleBird on how to use json.dumps to convert to JSON

https://www.w3schools.com/python/python_dictionaries_access.asp for information on how to get key and value from python dictionary


Contributors
============

* Mark Galloway
* Abram Hindle
* Cole Mackenzie
