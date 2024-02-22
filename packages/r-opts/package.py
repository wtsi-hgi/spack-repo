# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpts(RPackage):
	"""Optimization via Subsampling (OPTS)

	Subsampling based variable selection for low dimensional generalized linear models. The methods repeatedly subsample the data minimizing an information criterion (AIC/BIC) over a sequence of nested models for each subsample. Marinela Capanu, Mihai Giurcanu, Colin B Begg, Mithat Gonen, Subsampling based variable selection for generalized linear models. 
	"""
	
	cran = "OPTS" 

	version("0.1", md5="679dab1f09a271562b9db8be78e34477")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
