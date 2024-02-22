# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordcloud(RPackage):
	"""Word Clouds

	Functionality to create pretty word clouds, visualize differences and similarity between documents, and avoid over-plotting in scatter plots with text.
	"""
	
	homepage = "http://blog.fellstat.com/?cat=11"
	cran = "wordcloud" 

	version("2.6", md5="d672262f7673d26c469c12cd3e296ac7")

	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
