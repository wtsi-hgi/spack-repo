# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlogdown(RPackage):
	"""Create Blogs and Websites with R Markdown

	Write blog posts and web pages in R Markdown. This package
    supports the static site generator 'Hugo' (<https://gohugo.io>) best,
    and it also supports 'Jekyll' (<https://jekyllrb.com>) and 'Hexo'
    (<https://hexo.io>).
	"""
	
	homepage = "https://github.com/rstudio/blogdown"
	cran = "blogdown" 

	version("1.19", md5="ad9f344b43de3a37544e442fc6d88b0d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bookdown@0.22:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httpuv@1.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-knitr@1.25:", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
	depends_on("r-rmarkdown@2.8:", type=("build", "run"))
	depends_on("r-servr@0.21:", type=("build", "run"))
	depends_on("r-xfun@0.34:", type=("build", "run"))
	depends_on("r-yaml@2.1.19:", type=("build", "run"))
	depends_on("hugo", type=("build", "link", "run"))
