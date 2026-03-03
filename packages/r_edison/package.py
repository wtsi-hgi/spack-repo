# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdison(RPackage):
	"""Network Reconstruction and Changepoint Detection

	Package EDISON (Estimation of Directed Interactions from
    Sequences Of Non-homogeneous gene expression) runs an MCMC
    simulation to reconstruct networks from time series data, using
    a non-homogeneous, time-varying dynamic Bayesian network.
    Networks segments and changepoints are inferred concurrently,
    and information sharing priors provide a reduction of the
    inference uncertainty.
	"""
	
	cran = "EDISON" 

	version("1.1.1", md5="1f18d3a67b91b506b68e892d9c2c1ee7")

	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
