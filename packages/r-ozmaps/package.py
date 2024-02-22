# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROzmaps(RPackage):
	"""Australia Maps

	Maps of Australian coastline and administrative regions. Data 
 can be drawn or accessed directly as simple features objects. Includes
 simple functions for country or state maps of Australia and in-built data
 sets of administrative regions from the Australian Bureau of Statistics 
 <https://www.abs.gov.au/>. Layers include electoral divisions and local 
 government areas, simplified from the original sources but with sufficient 
 detail to allow mapping of a local municipality. 
	"""
	
	homepage = "https://github.com/mdsumner/ozmaps"
	cran = "ozmaps" 

	version("0.4.5", md5="dc3323dd9ca39fda45bb4357457c1b94")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-oz", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
