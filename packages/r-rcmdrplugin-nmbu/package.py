# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginNmbu(RPackage):
	"""R Commander Plug-in for University Level Applied Statistics

	An R Commander "plug-in" extending functionality of linear models
    and providing an interface to Partial Least Squares Regression and Linear and
    Quadratic Discriminant analysis. Several statistical summaries are extended,
    predictions are offered for additional types of analyses, and extra plots, tests
    and mixed models are available.
	"""
	
	homepage = "https://github.com/khliland/RcmdrPlugin.NMBU/"
	cran = "RcmdrPlugin.NMBU" 

	version("1.8.14", md5="1faa330a779aa776255ef29748bca50c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mixlm@1.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-phia", type=("build", "run"))
	depends_on("r-rcmdr@2.1.7:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
