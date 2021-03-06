# Laravel PHP Framework

[![Build Status](https://travis-ci.org/laravel/framework.svg)](https://travis-ci.org/laravel/framework)
[![Total Downloads](https://poser.pugx.org/laravel/framework/d/total.svg)](https://packagist.org/packages/laravel/framework)
[![Latest Stable Version](https://poser.pugx.org/laravel/framework/v/stable.svg)](https://packagist.org/packages/laravel/framework)
[![Latest Unstable Version](https://poser.pugx.org/laravel/framework/v/unstable.svg)](https://packagist.org/packages/laravel/framework)
[![License](https://poser.pugx.org/laravel/framework/license.svg)](https://packagist.org/packages/laravel/framework)
<br>
<code>$ cd /var/www/html</code>      
<code>$ git clone https://github.com/crew1274/web</code>      
<code>$ cd web</code>       
<code>$ composer install</code>     
<code>$ cp .env.example .env</code>     
> **Note:** 檢查 .env的設定，預設使用SQLite3，需要PHP SQLite Extension。   

<code>$ touch database/database.sqlite</code><br>
<code>$ php artisan key:generate</code><br>
<code>$ php artisan migrate --seed</code><br>
<code>$ cp storage/app/config_backup.json storage/app/config.json</code><br>
<code>$ sudo chmod 755 -R ../web/</code><br>
<code>$ sudo chmod o+w -R storage/</code><br>
<code>$ sudo vim /etc/apache2/sites-available/web.conf</code><br>
```sh
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/web/public

    <Directory /var/www/html/web>
        AllowOverride All
    </Directory>
```
<code>$ sudo a2dissite 000-default.conf</code>      
<code>$ sudo a2ensite web.conf</code>     
<code>$ sudo a2enmod rewrite</code>     
<code>$ sudo service apache2 restart</code>     
