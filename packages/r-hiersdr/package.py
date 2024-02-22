# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiersdr(RPackage):
	"""Hierarchical Sufficient Dimension Reduction

	Provides semiparametric sufficient dimension reduction for central mean subspaces for heterogeneous data defined by combinations of binary factors (such as chronic conditions). Subspaces are estimated to be hierarchically nested to respect the structure of subpopulations with overlapping characteristics. This package is an implementation of the proposed methodology of Huling and Yu (2021) <doi:10.1111/biom.13546>.
	"""
	
	cran = "hierSDR" 

	version("0.1", md5="07b7987456ca237f30ba058286accf88")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-lbfgs", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
