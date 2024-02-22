# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REm(RPackage):
	"""Generic EM Algorithm

	A generic function for running the Expectation-Maximization (EM) algorithm
  within a maximum likelihood framework, based on Dempster, Laird, and Rubin (1977) <doi:10.1111/j.2517-6161.1977.tb01600.x>
  is implemented. It can be applied after a model fitting using R's existing functions and packages.
	"""
	
	homepage = "https://github.com/wudongjie/em"
	cran = "em" 

	version("1.0.0", md5="4fe233c64e189d54ba88d3cf5cc7c558")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
