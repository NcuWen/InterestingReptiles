import os
import requests


def main():
    herolist_url = 'https://pvp.qq.com/web201605/js/herolist.json'
    response = requests.get(herolist_url).json()
    save_dir = 'D:\\Data\\Study\\Skin\\'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for i in range(len(response)):
        if 'skin_name' in response[i].keys():
            skin_names = response[i]['skin_name'].split('|')
        else:
            skin_names = response[i]['title'].split('|')
        for cnt in range(len(skin_names)):
            hero_num = response[i]['ename']
            hero_name = response[i]['cname']
            skin_name = skin_names[cnt]
            save_file_name = save_dir + str(hero_name) + '-' + skin_name + '.jpg'
            skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg' \
                .format(hero_num, hero_num, str(cnt + 1))
            response_skin_content = requests.get(skin_url).content
            with open(save_file_name, 'wb') as f:
                f.write(response_skin_content)
        print('正在下载第' + str(i + 1) + '/' + str(len(response)))


if __name__ == '__main__':
    main()
