# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhat(RPackage):
	"""General Likelihood Exploration

	Provides functions for Maximum Likelihood
             Estimation, Markov Chain Monte Carlo, finding confidence
             intervals.  The implementation is heavily based on the
             original Fortran source code translated to R.
	"""
	
	cran = "Bhat" 

	version("0.9-12", md5="ca2eb80a2d3407695b9fa9d01305e047")

	depends_on("r-mass", type=("build", "run"))
