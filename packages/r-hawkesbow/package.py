# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHawkesbow(RPackage):
	"""Estimation of Hawkes Processes from Binned Observations

	Implements an estimation method for Hawkes processes when count data are only observed in discrete time, using a spectral approach derived from the Bartlett spectrum, see Cheysson and Lang (2020) <arXiv:2003.04314>. Some general use functions for Hawkes processes are also included: simulation of (in)homogeneous Hawkes process, maximum likelihood estimation, residual analysis, etc.
	"""
	
	cran = "hawkesbow" 

	version("1.0.3", md5="71e5949c2895d8d020056b05bacc306f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
