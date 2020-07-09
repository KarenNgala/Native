from app import app
from flask import render_template
from .requests import sources, articles, headlines
import datetime as dt

@app.route('/')
def homepage():
    news_sources= sources()
    trending_article = headlines()
    print(trending_article)
    return render_template("index.html", news_sources=news_sources, trending_article=trending_article)

@app.route('/articles/<id>')
def all_articles(id):
    article_source = articles(id)
    print(article_source)
    return render_template("articles.html", article_source=article_source)
