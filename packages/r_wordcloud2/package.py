# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordcloud2(RPackage):
	"""Create Word Cloud by 'htmlwidget'

	A fast visualization tool for creating wordcloud
    by using 'wordcloud2.js'. 'wordcloud2.js' is a JavaScript library to create 
    wordle presentation on 2D canvas or HTML <https://timdream.org/wordcloud2.js/>.
	"""
	
	homepage = "https://github.com/lchiffon/wordcloud2"
	cran = "wordcloud2" 

	version("0.2.1", md5="299071535412b7053ad6b9e221e47f9b", url="https://cran.r-project.org/src/contrib/wordcloud2_0.2.1.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
