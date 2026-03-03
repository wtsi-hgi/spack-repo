# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrnagenetic(RPackage):
	"""Analysis of Small RNA Expression Changes in Hybrid Plants

	The most important function of the R package is the genetic effects analysis of small RNA in hybrid plants via two methods, and at the same time, it provides various forms of graph related to data characteristics and expression analysis. In terms of two classification methods, one is the calculation of the additive (a) and dominant (d), the other is the evaluation of expression level dominance by comparing the total expression of the small RNA in progeny with the expression level in the parent species.
	"""
	
	cran = "sRNAGenetic" 

	version("0.1.0", md5="6cb2a7c445d52935ac50c296551737ac")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
