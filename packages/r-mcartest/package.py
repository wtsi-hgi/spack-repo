# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcartest(RPackage):
	"""Optimal Nonparametric Testing of Missing Completely at Random

	Provides functions for carrying out nonparametric hypothesis tests of the MCAR hypothesis based on the theory of Frechet classes and compatibility. Also gives functions for computing halfspace representations of the marginal polytope and related geometric objects.
	"""
	
	cran = "MCARtest" 

	version("1.2.1", md5="156ec07c892aba0ebbec5734050ad12d")

	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-epi", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-highs", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcsdp", type=("build", "run"))
	depends_on("r-misty", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-missmethods", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
