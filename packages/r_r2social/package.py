# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2social(RPackage):
	"""App Inclusion of Social Sharing and Connect Buttons

	Implementation of 'JQuery' <https://jquery.com> and 'CSS' styles to allow easy incorporation of various social media elements on a page. The elements include addition of share buttons or connect with us buttons or hyperlink buttons to 'Shiny' applications or dashboards and 'Rmarkdown' documents.Sharing capability on social media platforms including 'Facebook' <https://www.facebook.com>, 'Linkedin' <https://www.linkedin.com>, 'X/Twitter' <https://x.com>, 'Tumblr' <https://www.tumblr.com>, 'Pinterest' <https://www.pinterest.com>, 'Whatsapp' <https://www.whatsapp.com>, 'Reddit' <https://www.reddit.com>, 'Baidu' <https://www.baidu.com>, 'Blogger' <https://www.blogger.com>, 'Weibo' <https://www.weibo.com>, 'Instagram' <https://www.instagram.com>, 'Telegram' <https://www.telegram.me>, 'Youtube' <https://www.youtube.com>.  
	"""
	
	homepage = "https://r2social.obi.obianom.com"
	cran = "r2social" 

	version("1.1", md5="08eac9f8b6ed8cdf787b4c29ce69aa12")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
