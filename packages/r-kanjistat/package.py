# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKanjistat(RPackage):
	"""A Statistical Framework for the Analysis of Japanese Kanji
Characters

	Various tools and data sets that support the study of kanji, including their morphology, decomposition and concepts of distance and similarity between them.
	"""
	
	homepage = "https://dschuhmacher.github.io/kanjistat/"
	cran = "kanjistat" 

	version("0.9.1", md5="3fd040c11441fbf3c2a85af3e8e708e9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-sysfonts", type=("build", "run"))
	depends_on("r-showtext", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
