class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_parameter):
        if isinstance(title_parameter, str) and 5 <= len(title_parameter) <= 50:
            self._title = title_parameter

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_parameter):
        if isinstance(author_parameter, Author):
            self._author = author_parameter
            author_parameter._articles.append(self)

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine_parameter):
        if isinstance(magazine_parameter, Magazine):
            self._magazine = magazine_parameter
            #add new article
            magazine_parameter._articles.append(self)

            


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = [] 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if (isinstance(name, str)) and (0 <len(name)) and not hasattr(self, "name"):
            self._name = name

    def articles(self):
        return self._articles
    
    def magazines(self):
        return list(set([article.magazine for article in self._articles]))
    
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))
    


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = [] 

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name_parameter):
        if isinstance(name_parameter, str) and 2 <= len(name_parameter) <= 16:
            self._name = name_parameter

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category_parameter):
        if isinstance(category_parameter, str) and 0 < len(category_parameter) <= 20:
            self._category = category_parameter

    def articles(self):
        return self._articles
    
    # def __repr__(self):
    #     return f"<Magazine: {self.name} ({self.category})>"
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def add_article(self, article):
        self._articles.append(article)

    def contributors(self):
        return list(set([article.author for article in self._articles]))

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None