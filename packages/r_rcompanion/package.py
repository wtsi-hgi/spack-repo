# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcompanion(RPackage):
	"""Functions to Support Extension Education Program Evaluation

	Functions and datasets to support Summary and Analysis of
             Extension Program Evaluation in R, and An R
             Companion for the Handbook of Biological Statistics. 
             Vignettes are available at <https://rcompanion.org>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=rcompanion"
	cran = "rcompanion" 

	version("2.4.35", md5="a83bd4f9af6c634c5b4fee480733bef5")
	version("2.4.26", md5="97cff8fefc8cc0bf0f0eff96b49779e1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-boot@1.3.28:", type=("build", "run"))
	depends_on("r-desctools@0.99.43:", type=("build", "run"))
	depends_on("r-multcompview@0.1.8:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-coin@1.4.2:", type=("build", "run"))
	depends_on("r-lmtest@0.9.38:", type=("build", "run"))
	depends_on("r-nortest@1.0.4:", type=("build", "run"))
