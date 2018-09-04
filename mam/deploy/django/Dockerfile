FROM python

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

RUN mkdir /code/db

WORKDIR /code

ADD ./requirements.txt /code/

RUN pip install --no-cache-dir -r requirement.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

ADD . /code/

#暴露端口8000，到时候执行docker run 的时候才好把宿主机端口映射到8000
EXPOSE 8000
