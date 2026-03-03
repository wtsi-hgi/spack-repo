# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayespo(RPackage):
	"""Bayesian Inference for Presence-Only Data

	Presence-Only data is best modelled with a Point Process Model.
    The work of Moreira and Gamerman (2022) <doi:10.1214/21-AOAS1569> provides
    a way to use exact Bayesian inference to model this type of data, which is
    implemented in this package.
	"""
	
	cran = "bayesPO" 

	version("0.5.0", md5="082ceb5dc330459f596a23e6dc1b105e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
