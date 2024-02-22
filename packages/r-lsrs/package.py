# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsrs(RPackage):
	"""Land Surface Remote Sensing

	Rapid satellite data streams in operational applications
    have clear benefits for monitoring land cover, 
    especially when information can be delivered as fast as changing
    surface conditions. Over the past decade,
    remote sensing has become a key tool for monitoring and predicting
    environmental variables by using satellite data. 
    This package presents the main applications in remote sensing for 
    land surface monitoring and land cover mapping (soil, vegetation, water...).
     Tomlinson, C.J., Chapman, L., Thornes, E., Baker, C (2011) <doi:10.1002/met.287>.
	"""
	
	cran = "LSRS" 

	version("0.2.0", md5="00d6f513bac044761bad39877af7daa6")

