# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStates(RPackage):
	"""Create Panels of Independent States

	Create panel data consisting of independent states from 1816 to
    the present. The package includes the Gleditsch & Ward (G&W) and Correlates
    of War (COW) lists of independent states, as well as helper functions for 
    working with state panel data and standardizing other data sources to 
    create country-year/month/etc. data. 
	"""
	
	homepage = "https://github.com/andybega/states"
	cran = "states" 

	version("0.3.2", md5="d7f50c5bd7c28fe67aa55cedda54d40d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
