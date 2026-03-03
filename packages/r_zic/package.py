# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZic(RPackage):
	"""Bayesian Inference for Zero-Inflated Count Models

	Provides MCMC algorithms for the analysis of
        zero-inflated count models. The case of stochastic search
        variable selection (SVS) is also considered.  All MCMC samplers
        are coded in C++ for improved efficiency. A data set
        considering the demand for health care is provided.
	"""
	
	cran = "zic" 

	version("0.9.1", md5="2c5187aa86759ea62b54dea27989ecc9")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda@0.14.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
