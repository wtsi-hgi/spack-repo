# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmpathcr(RPackage):
	"""Fit a Penalized Continuation Ratio Model for Predicting an
Ordinal Response

	Provides a function for fitting a penalized constrained  continuation ratio model using the glmpath algorithm and methods for  extracting coefficient estimates, predicted class, class probabilities, and plots as described by Archer and Williams (2012) <doi:10.1002/sim.4484>. 
	"""
	
	cran = "glmpathcr" 

	version("1.0.10", md5="da762f288315f26f58e8109f2abe8834")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-glmpath", type=("build", "run"))
