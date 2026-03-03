# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrbin(RPackage):
	"""Nonparametrics with Clustered Binary and Multinomial Data

	Implements non-parametric analyses for clustered
    binary and multinomial data. The elements of the cluster are assumed
    exchangeable, and identical joint distribution (also known as marginal
    compatibility, or reproducibility) is assumed for clusters of different
    sizes. A trend test based on stochastic ordering is implemented. 
    Szabo A, George EO. (2010) <doi:10.1093/biomet/asp077>;
    George EO, Cheon K, Yuan Y, Szabo A (2016) <doi:10.1093/biomet/asw009>.
	"""
	
	cran = "CorrBin" 

	version("1.6.1", md5="71d5dcae45075e2df86b543043e3b85d")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-dirmult", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
