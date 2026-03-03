# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGunsales(RPackage):
	"""Statistical Analysis of Monthly Background Checks of Gun
Purchases

	Statistical analysis of monthly background checks of gun purchases for the New York Times 
 story "What Drives Gun Sales: Terrorism, Obama and Calls for Restrictions" at 
 <http://www.nytimes.com/interactive/2015/12/10/us/gun-sales-terrorism-obama-restrictions.html?> is provided.
	"""
	
	cran = "gunsales" 

	version("0.1.2", md5="437a0758c61f65bfe06ff3b9c1fabd79")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-seasonal", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-x13binary", type=("build", "run"))
