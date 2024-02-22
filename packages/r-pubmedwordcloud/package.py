# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPubmedwordcloud(RPackage):
	"""'Pubmed' Word Clouds

	Create a word cloud using the abstract of publications from 'Pubmed'.
	"""
	
	homepage = "http://felixfan.github.io/PubMedWordcloud/"
	cran = "PubMedWordcloud" 

	version("0.3.6", md5="5e73eed2f0f925cd54d84ccb61319578")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-wordcloud", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
