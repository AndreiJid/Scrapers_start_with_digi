#!/usr/bin/env bash
#
# make a curl requests from bash

bash_response=$(curl 'https://www.autototal.ro/wp-admin/admin-ajax.php' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-US,en;q=0.6' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Cookie: CEqlFzZrn=kh%2AcZJjfU; PaZJDSV_wncxO=RBJb8h' \
  -H 'Origin: https://www.autototal.ro' \
  -H 'Referer: https://www.autototal.ro/cariere/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-GPC: 1' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  --data-raw 'data%5Bblog_style%5D=justified-3x&data%5Bjustified_style%5D=justified-style-1&data%5Bslider_style%5D=fullwidth&data%5Bslider_autoscroll%5D=0&data%5Bsource_type%5D=custom&data%5Bselect_blog_categories%5D=1&data%5Bblog_categories%5D=cariere&data%5Bselect_blog_tags%5D=1&data%5Bblog_tags%5D=&data%5Bselect_blog_posts%5D=1&data%5Bblog_posts%5D=&data%5Bselect_blog_authors%5D=&data%5Bblog_authors%5D=&data%5Bblog_order_by%5D=default&data%5Bblog_order%5D=default&data%5Bblog_offset%5D=&data%5Bblog_exclude_posts%5D=&data%5Bblog_post_per_page%5D=9&data%5Bblog_post_types%5D%5B%5D=post&data%5Bblog_post_types%5D%5B%5D=thegem_news&data%5Bblog_pagination%5D=more&data%5Bblog_ignore_sticky%5D=&data%5Bis_ajax%5D=0&data%5Bpaged%5D=Z&data%5Beffects_enabled%5D=0&data%5Bloading_animation%5D=move-up&data%5Bshow_title%5D=1&data%5Btruncate_title%5D=0&data%5Btitle_size%5D=25&data%5Bhide_featured%5D=0&data%5Bhide_date%5D=1&data%5Bhide_author%5D=1&data%5Bhide_comments%5D=1&data%5Bhide_likes%5D=1&data%5Bshow_category%5D=1&data%5Bshow_description%5D=1&data%5Btruncate_description%5D=0&data%5Bdescription_size%5D=25&data%5Bshow_separator%5D=1&data%5Bbutton%5D%5Btext%5D=MAI+MULT&data%5Bbutton%5D%5Bstyle%5D=flat&data%5Bbutton%5D%5Bsize%5D=medium&data%5Bbutton%5D%5Btext_weight%5D=normal&data%5Bbutton%5D%5Bno_uppercase%5D=0&data%5Bbutton%5D%5Bcorner%5D=25&data%5Bbutton%5D%5Bborder%5D=2&data%5Bbutton%5D%5Btext_color%5D=&data%5Bbutton%5D%5Bbackground_color%5D=%23108642&data%5Bbutton%5D%5Bborder_color%5D=&data%5Bbutton%5D%5Bhover_text_color%5D=&data%5Bbutton%5D%5Bhover_background_color%5D=&data%5Bbutton%5D%5Bhover_border_color%5D=&data%5Bbutton%5D%5Bicon_pack%5D=elegant&data%5Bbutton%5D%5Bicon_elegant%5D=&data%5Bbutton%5D%5Bicon_material%5D=&data%5Bbutton%5D%5Bicon_fontawesome%5D=&data%5Bbutton%5D%5Bicon_thegem_header%5D=&data%5Bbutton%5D%5Bicon_userpack%5D=&data%5Bbutton%5D%5Bicon_position%5D=left&data%5Bbutton%5D%5Bseparator%5D=load-more&data%5Bbutton%5D%5Bicon%5D=&data%5Bitem_colors%5D%5Bbackground_color%5D=&data%5Bitem_colors%5D%5Bpost_title_color%5D=&data%5Bitem_colors%5D%5Bpost_title_hover_color%5D=&data%5Bitem_colors%5D%5Bpost_excerpt_color%5D=&data%5Bitem_colors%5D%5Bsharing_button_color%5D=&data%5Bitem_colors%5D%5Bsharing_button_icon_color%5D=&data%5Bitem_colors%5D%5Btime_line_color%5D=&data%5Bitem_colors%5D%5Bmonth_color%5D=&data%5Bitem_colors%5D%5Bdate_color%5D=&data%5Bitem_colors%5D%5Btime_color%5D=&data%5Bitem_colors%5D%5Bborder_color%5D=&data%5Bitem_colors%5D%5Badditional_background_color%5D=&data%5Bbottom_gap%5D=&data%5Bimage_size%5D=&data%5Bimage_border_radius%5D=&data%5Btitle_preset%5D=default&data%5Btitle_transform%5D=&data%5Bpost_excerpt_preset%5D=text-body-tiny&data%5Bhover_overlay_color%5D=&data%5Bicon_on_hover%5D=1&data%5Bimage_height%5D=&data%5Bfullwidth_section_images%5D=&data%5Brelated_by_categories%5D=1&data%5Brelated_by_tags%5D=&data%5Brelated_by_author%5D=&data%5Bhide_social_sharing%5D=0&url=https%3A%2F%2Fwww.autototal.ro%2Fwp-admin%2Fadmin-ajax.php&nonce=2bd6e27a96&action=blog_load_more&SvJRPm_yZWH=u4CULE8cpFRO&FxunpVCSADPLMbW=st_U7a]Z' \
  --compressed)

echo $bash_response
