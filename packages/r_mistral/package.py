# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMistral(RPackage):
	"""Methods in Structural Reliability

	Various reliability analysis methods for rare event inference (computing failure probability and quantile from model/function outputs).
	"""
	
	cran = "mistral" 

	version("2.2.2", md5="9ec07b169628f272972e4dab6dac624f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-dicekriging", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
