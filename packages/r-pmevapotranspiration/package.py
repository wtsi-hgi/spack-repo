# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmevapotranspiration(RPackage):
	"""Calculation of the Penman-Monteith Evapotranspiration using
Weather Variables

	The Food and Agriculture Organization-56 Penman-Monteith is one of the important method for estimating evapotranspiration from vegetated land areas. This package helps to calculate reference evapotranspiration using the weather variables collected from weather station. Evapotranspiration is the process of water transfer from the land surface to the atmosphere through evaporation from soil and other surfaces and transpiration from plants. The package aims to support agricultural, hydrological, and environmental research by offering accurate and accessible reference evapotranspiration calculation. This package has been developed using concept of Córdova et al. (2015)<doi:10.1016/j.apm.2022.09.004> and Debnath et al. (2015) <doi:10.1007/s40710-015-0107-1>.
	"""
	
	cran = "PMEvapotranspiration" 

	version("0.1.0", md5="616af86a60d79085ab1add39efd17c65")

