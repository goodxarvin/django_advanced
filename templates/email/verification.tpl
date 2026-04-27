{% extends "mail_templated/base.tpl" %}

{% block subject %}
email verification
{% endblock %}


{% block body %}

{% endblock %}

{% block html %}


here is an image

<html>
<body>
    <h1>Hello {{ name }}, {{id }}</h1>
    <p>here is your access token:</p>
    <a>http://127.0.0.1:8001/accounts/api/v1/verification/confirm/{{ access_token }}</a>
    <img src="https://dkstatics-public.digikala.com/digikala-adservice-banners/2d35faad146a8794dce0cf31501c27ae4378b9aa_1777274902.jpg?x-oss-process=image/quality,q_95/format,webp">

</body>
</html>

{% endblock %}
