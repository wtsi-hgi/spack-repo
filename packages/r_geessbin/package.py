# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeessbin(RPackage):
	"""Modified Generalized Estimating Equations for Binary Outcome

	Analyze small-sample clustered or longitudinal data with binary 
    outcome using modified generalized estimating equations with bias-adjusted
    covariance estimator. The package provides any combination of three 
    modified generalized estimating equations and 11 bias-adjusted covariance 
    estimators.
	"""
	
	homepage = "https://github.com/rtishii/geessbin"
	cran = "geessbin" 

	version("0.1.2", md5="eb0afda883252abfd904c5c6e99f76b4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
