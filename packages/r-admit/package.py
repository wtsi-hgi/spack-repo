# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmit(RPackage):
	"""Adaptive Mixture of Student-t Distributions

	Provides functions to perform the fitting of an adaptive mixture
    of Student-t distributions to a target density through its kernel function as described in
    Ardia et al. (2009) <doi:10.18637/jss.v029.i03>. The
    mixture approximation can then be used as the importance density in importance
    sampling or as the candidate density in the Metropolis-Hastings algorithm to
    obtain quantities of interest for the target density itself. 
	"""
	
	homepage = "https://github.com/ArdiaD/AdMit"
	cran = "AdMit" 

	version("2.1.9", md5="720ee7e2036f20e965e384e79814b6b7")

	depends_on("r-mvtnorm", type=("build", "run"))
