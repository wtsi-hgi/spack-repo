# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatespacer(RPackage):
	"""State Space Modelling in 'R'

	A tool that makes estimating models in state space form 
    a breeze. See "Time Series Analysis by State Space Methods" by 
    Durbin and Koopman (2012, ISBN: 978-0-19-964117-8) for details 
    about the algorithms implemented.
	"""
	
	homepage = "https://DylanB95.github.io/statespacer/"
	cran = "statespacer" 

	version("0.5.0", md5="0cd33f606776b7c7ec4eb5fed8a9fa6b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
