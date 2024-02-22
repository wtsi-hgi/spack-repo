# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParma(RPackage):
	"""Portfolio Allocation and Risk Management Applications

	Provision of a set of models and methods for use in the allocation and management of capital in financial portfolios.
	"""
	
	homepage = "https://github.com/alexiosg/parma"
	cran = "parma" 

	version("1.7", md5="39ad881d19b65fa34cca97a78a16a770")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
