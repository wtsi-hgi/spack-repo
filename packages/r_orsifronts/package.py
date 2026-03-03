# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrsifronts(RPackage):
	"""Southern Ocean Frontal Distributions (Orsi)

	A data set package with the "Orsi" and "Park/Durand" fronts as
    'SpatialLinesDataFrame' objects. The Orsi et al. (1995) fronts are published at
    the Southern Ocean Atlas Database Page, and the Park et al. (2019) fronts are published at the 'SEANOE' 
    Altimetry-derived Antarctic Circumpolar Current fronts page, please see package CITATION for details.
	"""
	
	homepage = "https://australianantarcticdivision.github.io/orsifronts/"
	cran = "orsifronts" 

	version("0.2.0", md5="9699dc554f330328592a6350a3c7b813")

	depends_on("r-sp", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
