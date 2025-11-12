---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<span class='anchor' id='about-me'></span>

{% include_relative includes/intro.md %}

{% include_relative includes/others.md %}

{% include_relative includes/honers.md %}

{% include_relative includes/pub.md %}


<a href="https://info.flagcounter.com/aBrJ"><img src="https://s01.flagcounter.com/count2/aBrJ/bg_FFFFFF/txt_000000/border_CCCCCC/columns_8/maxflags_20/viewers_0/labels_1/pageviews_1/flags_0/percent_0/" alt="Flag Counter" border="0"></a>

<div style="width: 500px; max-width: 100%; height: auto; overflow: hidden; margin: 0 auto; text-align: center;">
    <!-- ClustrMaps Visitor Map - 使用静态图片作为可靠显示 -->
    <a href="https://clustrmaps.com/site/1b2x" title="Visitor Map" target="_blank" rel="noopener noreferrer">
        <img src="https://www.clustrmaps.com/map_v2.png?d=QUwhfA7E5hbbJECoaXHjBrEzdt9cHqDRrK58A9pJY4s&cl=ffffff" alt="Visitor Map" style="border:0; max-width:100%; height:auto;" />
    </a>

    <!-- 尝试加载动态地图（如果脚本加载成功，会在地图上叠加交互功能） -->
    <script type="text/javascript">
        (function() {
            // 延迟加载 ClustrMaps 脚本，避免阻塞页面渲染
            window.addEventListener('load', function() {
                setTimeout(function() {
                    var script = document.createElement('script');
                    script.type = 'text/javascript';
                    script.async = true;
                    script.defer = true;
                    script.src = 'https://clustrmaps.com/map_v2.js?d=QUwhfA7E5hbbJECoaXHjBrEzdt9cHqDRrK58A9pJY4s&cl=ffffff&w=a';
                    
                    script.onerror = function() {
                        // 脚本加载失败时，静态图片仍会显示，这是正常的
                        console.log('ClustrMaps interactive map unavailable, static image displayed');
                    };
                    
                    (document.head || document.body).appendChild(script);
                }, 500);
            });
        })();
    </script>
</div>

<div style="text-align: center; font-size: small;">
  Last updated on 2025/11/12
</div>
