# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgsolvencyii(RPackage):
	"""A 'ggplot2'-Plot of Composition of Solvency II SCR: SF and IM

	An implementation of 'ggplot2'-methods to present the composition of Solvency II Solvency Capital Requirement (SCR) as a series of concentric circle-parts. 
 Solvency II (Solvency 2) is European insurance legislation, coming in force by the delegated acts of October 10, 2014.
 <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ%3AL%3A2015%3A012%3ATOC>. 
 Additional files, defining the structure of the Standard Formula (SF) method of the SCR-calculation are provided.
 The structure files can be adopted for localization or for insurance companies who use Internal Models (IM).
 Options are available for combining smaller components, horizontal and vertical scaling, rotation, and plotting only some circle-parts.
 With outlines and connectors several SCR-compositions can be compared, for example in ORSA-scenarios (Own Risk and Solvency Assessment).
	"""
	
	homepage = "https://github.com/vanzanden/ggsolvencyii"
	cran = "ggsolvencyii" 

	version("0.1.2", md5="0d1e9c66a4519d55a99397f703719519")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
