## 調査項目

- Group がいわゆるロールの扱いとして利用できるか
- Group はどのように作成するか
- Group にどうやってパーミッションを付加するか
- Group にどうやってユーザーを追加削除するか
- User にパーミッションを追加するやり方
- view またはテンプレートでパーミッションの制御を行う方法

# 調査結果

1.. Group がいわゆるロールの扱いとして利用できるか
=> 扱えると判断

2.. Group はどのように作成するか
=> 方法は複数ある。django のアドミンから作成するのが一番簡単。
その他 shell から作成する方法もある。

3.. Group にどうやってパーミッションを付加するか
Group と permisson は manytomany の関係にあるので、そんな感じで ORM 操作すれば付加できる。
ex. group.add(permission)
また、admin からパーミッションを追加することもできる

4.. Group にどうやってユーザーを追加削除するか
3 とおなじ

5.. view またはテンプレートでパーミッションの制御を行う方法
login_required 等のデコレータが存在していることは知っていたが、これは Class based View
で利用する事ができないと判明。
Class based View の場合 mixin を使ってパーミッションによるアクセス制御を行う事がわかった。

User パーミッションの調査のための User を作る
Blog をリソースとする
まず何も権限が与えられていない User によるアクセス
Blog の権限が与えられている User によるアクセス
Blog の権限が与えられている Group に属する User によるアクセス

```python
## ---3種類のユーザを作成する---
# パーミッションがないユーザーを作成
from django.contrib.auth.models import User
no_perisson_user_data = {'username':'no_permisson_user', 'email': 'no_permisson_user@maill.com', 'password':'pass1234'}
User.objects.create_user(username=no_perisson_user_data['username'], email=no_perisson_user_data['email'], password=no_perisson_user_data['password'])
# パーミッションがあるユーザーを作成
perisson_user_data = {'username':'permisson_user', 'email': 'permisson_user@maill.com', 'password':'pass1234'}
User.objects.create_user(username=perisson_user_data['username'], email=perisson_user_data['email'], password=perisson_user_data['password'])
# パーミッションを有するグループに属するユーザーを作成
group_user_data = {'username':'group_user', 'email': 'group_user@maill.com', 'password':'pass1234'}
User.objects.create_user(username=group_user_data['username'], email=group_user_data['email'], password=group_user_data['password'])

## ---パーミッションをセットする---
# Groupオブジェクトを作成
from django.contrib.auth.models import Group
blog_view_group = Group.objects.create(name='blog_view_group')
# GroupオブジェクトにUserオブジェクトを紐づける
group_user = User.objects.get(name=group_user_data['username'])
group_user.groups.set([blog_view_group])
# Permissonオブジェクトを作成
from django.contrib.auth.models import Permission
# 作成したGroupにPermissonオブジェクトを紐づける
blog_view_permission = Permission.objects.get(name=`Can view blog`)
blog_view_group.permissions.set([blog_view_permission])

## 準備完了 試してみる
from django.test import TestCase
class BlogViewTest(TestCase):
    def test_no_permisson_user_view(self):
        url = '/blogs/'
        self.client = Client()
        login_status = self.client.login(username=no_perisson_user_data['username'], password=no_perisson_user_data['password'])
        self.asserttrue(login_status)
        response = self.client.get(url)
        print(response)






```
