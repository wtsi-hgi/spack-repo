# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsectdisease(RPackage):
	"""Ecological Database of the World's Insect Pathogens

	David Onstad provided us with this insect disease database, sometimes referred to as the 'Ecological Database of the Worlds Insect Pathogens' or EDWIP. Files have been converted from 'SQL' to csv, and ported into 'R' for easy exploration and analysis. Thanks to the Macroecology of Infectious Disease Research Coordination Network (RCN) for funding and support. Data are also served online in a static format at <https://edwip.ecology.uga.edu/>. 
	"""
	
	cran = "insectDisease" 

	version("1.2.2", md5="4a694a07e73eb425046b1d6a3f209c52")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
