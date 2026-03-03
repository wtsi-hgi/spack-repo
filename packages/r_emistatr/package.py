# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmistatr(RPackage):
	"""Emissions and Statistics in R for Wastewater and Pollutants in
Combined Sewer Systems

	Provides a fast and parallelised calculator to estimate combined wastewater emissions. 
    It supports the planning and design of urban drainage systems, without the requirement of 
    extensive simulation tools. The 'EmiStatR' package implements modular R methods. This enables 
    to add new functionalities through the R framework. 
	"""
	
	cran = "EmiStatR" 

	version("1.2.3.0", md5="07edbae22c1f805f7f106234777f78ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
