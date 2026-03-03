# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGbj(RPackage):
	"""Generalized Berk-Jones Test for Set-Based Inference in Genetic
Association Studies

	Offers the Generalized Berk-Jones (GBJ) test for set-based inference in genetic
	association studies. The GBJ is designed as an alternative to tests such as Berk-Jones (BJ),
    Higher Criticism (HC), Generalized Higher Criticism (GHC), Minimum p-value (minP), and Sequence
    Kernel Association Test (SKAT). All of these other methods (except for SKAT) are also implemented 
    in this package, and we additionally provide an omnibus test (OMNI) which integrates information from each of the tests.
    The GBJ has been shown to outperform other tests in genetic association studies when signals
    are correlated and moderately sparse. Please see the vignette for a quickstart guide or Sun and Lin
    (2017) <arXiv:1710.02469> for more details.
	"""
	
	cran = "GBJ" 

	version("0.5.4", md5="eb54f488a97d8cb2f03c5f5d9ff2ab74")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-skat", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
