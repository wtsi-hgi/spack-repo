# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlap(RPackage):
	"""Forecast Linear Augmented Projection

	The Forecast Linear Augmented Projection (flap) method reduces 
    forecast variance by adjusting the forecasts of multivariate time series to 
    be consistent with the forecasts of linear combinations (components) of the 
    series by projecting all forecasts onto the space where the linear 
    constraints are satisfied. The forecast variance can be reduced 
    monotonically by including more components. For a given number of 
    components, the flap method achieves maximum forecast variance reduction 
    among linear projections. 
	"""
	
	homepage = "https://github.com/FinYang/flap"
	cran = "flap" 

	version("0.1.0", md5="f8691ef5c73992dc477af4e3c49b43ed")

	depends_on("r-corpcor", type=("build", "run"))
