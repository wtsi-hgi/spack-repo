# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVinereg(RPackage):
	"""D-Vine Quantile Regression

	
  Implements D-vine quantile regression models with
  parametric or nonparametric pair-copulas. See 
  Kraus and Czado (2017) <doi:10.1016/j.csda.2016.12.009> and
  Schallhorn et al. (2017) <arXiv:1705.08310>.
	"""
	
	homepage = "https://tnagler.github.io/vinereg/"
	cran = "vinereg" 

	version("0.10.0", md5="fcc6aa827b9ddc6b36f9b221a7e40d18")

	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-kde1d", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
