# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrocode(RPackage):
	"""Hydrological Codes

	Pfafstetter Hydrological Codes 
    as cited in Verdin and Verdin (1999) <doi: 10.1016/S0022-1694(99)00011-6> 
    are decoded for upstream or downstream queries.
	"""
	
	cran = "HydroCode" 

	version("1.0.3", md5="5b9bd2eb35fca6bab1422b069e65f503")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
