# The "image is AI-generated" icon

This project provides a simple way to mark your images as AI-generated.

There can be many reasons to do this, such as regulations like the EU AI Act.

The solution: just add a recognizable icon to the image. 

# The icon

This project provides a free and open-source icon exactly for that. 
It is realeased into the public domain, meaning you can use it for any purpose without any restrictions.

The icon comes in three versions:

<table><tr>
<td><a href="icon/png/white_on_black.png" target="_blank"><img src="icon/png/white_on_black.png" width="100"></a></td>
<td><a href="icon/png/white_on_blue.png" target="_blank"><img src="icon/png/white_on_blue.png" width="100"></a></td>
<td><a href="icon/png/black_on_white.png" target="_blank"><img src="icon/png/black_on_white.png" width="100"></a></td>
</tr></table>

We also have SVG [versions](icon/svg), including a black-on-transparent one.

We recommend using the blue version, as it looks good on both light and dark backgrounds.
But feel free to use any of them.



# Usage exmaples

(Click to see the full-size image)

White on black icon:
<table><tr>

<td><a href="examples/with_icon_white_on_black/summer_with_icon_white_on_black.png" target="_blank"><img src="examples/with_icon_white_on_black/summer_with_icon_white_on_black.png" width="300"></a></td>
<td><a href="examples/with_icon_white_on_black/winter_with_icon_white_on_black.png" target="_blank"><img src="examples/with_icon_white_on_black/winter_with_icon_white_on_black.png" width="300"></a></td>
<td><a href="examples/with_icon_white_on_black/night_with_icon_white_on_black.png" target="_blank"><img src="examples/with_icon_white_on_black/night_with_icon_white_on_black.png" width="300"></a></td>
</tr></table>

White on blue icon:
<table><tr>
<td><a href="examples/with_icon_white_on_blue/summer_with_icon_white_on_blue.png" target="_blank"><img src="examples/with_icon_white_on_blue/summer_with_icon_white_on_blue.png" width="300"></a></td>
<td><a href="examples/with_icon_white_on_blue/winter_with_icon_white_on_blue.png" target="_blank"><img src="examples/with_icon_white_on_blue/winter_with_icon_white_on_blue.png" width="300"></a></td>
<td><a href="examples/with_icon_white_on_blue/night_with_icon_white_on_blue.png" target="_blank"><img src="examples/with_icon_white_on_blue/night_with_icon_white_on_blue.png" width="300"></a></td>
</tr></table>

Black on white icon:
<table><tr>
<td><a href="examples/with_icon_black_on_white/summer_with_icon_black_on_white.png" target="_blank"><img src="examples/with_icon_black_on_white/summer_with_icon_black_on_white.png" width="300"></a></td>
<td><a href="examples/with_icon_black_on_white/winter_with_icon_black_on_white.png" target="_blank"><img src="examples/with_icon_black_on_white/winter_with_icon_black_on_white.png" width="300"></a></td>
<td><a href="examples/with_icon_black_on_white/night_with_icon_black_on_white.png" target="_blank"><img src="examples/with_icon_black_on_white/night_with_icon_black_on_white.png" width="300"></a></td>
</tr></table>

# Recommended usage

We recommend placing the icon in the bottom-right corner of the image. 

We recommend scaling the icon's height to 1/40th of the image's height, 
with a 1/100th padding (see the `add_icon.py` script for a reference implementation).

# Icon design considerations

1) It says "AI". 

2) The icon is readable by both English and Chinese speakers, thus automatically covering about
20% of the world population. 
Due to a lucky coincidence, Chinese for "artificial" looks like "AI": 人工.

3) It has a simple but unique design. If you saw it once, you'll easily recognize it. 

4. It scales well and looks good even at small sizes. 

5. It works well on both light and dark backgrounds. 

6. It's unobtrusive and doesn't distract from the image's content. 

# License

This project is released into the public domain. Use it without any restrictions. 
