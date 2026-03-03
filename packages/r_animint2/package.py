# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnimint2(RPackage):
	"""Animated Interactive Grammar of Graphics

	Functions are provided for defining animated,
 interactive data visualizations in R code, and rendering
 on a web page. The 2018 Journal of Computational and 
 Graphical Statistics paper,
 <doi:10.1080/10618600.2018.1513367>
 describes the concepts implemented.
	"""
	
	homepage = "https://animint.github.io/animint2/"
	cran = "animint2" 

	version("2024.1.24", md5="407ca67f0bde2f26af18c128e2a58b56", url="https://cran.r-project.org/src/contrib/animint2_2024.1.24.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-gtable@0.1.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr@1.7.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
	depends_on("r-knitr@1.5.33:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
