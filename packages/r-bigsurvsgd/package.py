# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigsurvsgd(RPackage):
	"""Big Survival Analysis Using Stochastic Gradient Descent

	Fits Cox model via stochastic gradient descent. This implementation avoids computational instability of the standard Cox Model when dealing large datasets. Furthermore, it scales up with large datasets that do not fit the memory. It also handles large sparse datasets using proximal stochastic gradient descent algorithm. For more details about the method, please see Aliasghar Tarkhan and Noah Simon (2020) <arXiv:2003.00116v2>.
	"""
	
	cran = "bigSurvSGD" 

	version("0.0.1", md5="1b0db5ab71169133d211e8ec18e23c93")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
