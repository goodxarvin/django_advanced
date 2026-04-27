{% extends "mail_templated/base.tpl" %}

{% block subject %}
email verification
{% endblock %}


{% block body %}

{% endblock %}

{% block html %}


متن ساده برای کلاینت‌هایی که HTML ساپورت نمی‌کنند.

<html>
<body>
    <h1>سلام!</h1>
    <!-- لینک عکس حتماً باید کامل (Absolute) و ترجیحاً HTTPS باشد -->
    <img src="https://dkstatics-public.digikala.com/digikala-adservice-banners/2d35faad146a8794dce0cf31501c27ae4378b9aa_1777274902.jpg?x-oss-process=image/quality,q_95/format,webp">

</body>
</html>

{% endblock %}
