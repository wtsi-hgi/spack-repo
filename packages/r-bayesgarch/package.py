# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgarch(RPackage):
	"""Bayesian Estimation of the GARCH(1,1) Model with Student-t
Innovations

	Provides the bayesGARCH() function which performs the
    Bayesian estimation of the GARCH(1,1) model with Student's t innovations as described in Ardia (2008) <doi:10.1007/978-3-540-78657-3>.
	"""
	
	homepage = "https://github.com/ArdiaD/bayesGARCH"
	cran = "bayesGARCH" 

	version("2.1.10", md5="24a9b2ae32c6b0e1575dafad8617dcba")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
