Python 3.7.8 (tags/v3.7.8:4b47a5b6ba, Jun 28 2020, 08:53:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\java\cn\anusha\diabetics prediction.py ==============
Traceback (most recent call last):
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1350, in do_open
    encode_chunked=req.has_header('Transfer-encoding'))
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1262, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1308, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1257, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1028, in _send_output
    self.send(msg)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 968, in send
    self.connect()
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 1424, in connect
    super().connect()
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\http\client.py", line 940, in connect
    (self.host,self.port), self.timeout, self.source_address)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\socket.py", line 707, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\socket.py", line 752, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 11001] getaddrinfo failed

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\java\cn\anusha\diabetics prediction.py", line 12, in <module>
    data = pd.read_csv(url, names=column_names)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\util\_decorators.py", line 311, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers\readers.py", line 586, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers\readers.py", line 482, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers\readers.py", line 811, in __init__
    self._engine = self._make_engine(self.engine)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers\readers.py", line 1040, in _make_engine
    return mapping[engine](self.f, **self.options)  # type: ignore[call-arg]
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers\c_parser_wrapper.py", line 51, in __init__
    self._open_handles(src, kwds)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\parsers\base_parser.py", line 229, in _open_handles
    errors=kwds.get("encoding_errors", "strict"),
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\common.py", line 614, in get_handle
    storage_options=storage_options,
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\common.py", line 312, in _get_filepath_or_buffer
    with urlopen(req_info) as req:
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\site-packages\pandas\io\common.py", line 212, in urlopen
    return urllib.request.urlopen(*args, **kwargs)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 222, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 525, in open
    response = self._open(req, data)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 543, in _open
    '_open', req)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 503, in _call_chain
    result = func(*args)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1393, in https_open
    context=self._context, check_hostname=self._check_hostname)
  File "C:\Users\sanep\AppData\Local\Programs\Python\Python37\lib\urllib\request.py", line 1352, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [Errno 11001] getaddrinfo failed>
>>> 
============== RESTART: C:\java\cn\anusha\diabetics prediction.py ==============
Accuracy: 0.7532467532467533
Confusion Matrix:
 [[79 20]
 [18 37]]
Classification Report:
               precision    recall  f1-score   support

           0       0.81      0.80      0.81        99
           1       0.65      0.67      0.66        55

    accuracy                           0.75       154
   macro avg       0.73      0.74      0.73       154
weighted avg       0.76      0.75      0.75       154

>>> 
============== RESTART: C:\java\cn\anusha\diabetics prediction.py ==============
Accuracy: 0.7532467532467533
Confusion Matrix:
 [[79 20]
 [18 37]]
Classification Report:
               precision    recall  f1-score   support

           0       0.81      0.80      0.81        99
           1       0.65      0.67      0.66        55

    accuracy                           0.75       154
   macro avg       0.73      0.74      0.73       154
weighted avg       0.76      0.75      0.75       154

>>> 