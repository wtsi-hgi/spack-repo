# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REiDatasets(RPackage):
	"""Real Datasets for Assessing Ecological Inference Algorithms

	Provides more than 550 data sets of actual election results. 
    Each of the data sets includes aggregate party and candidate outcomes at the voting
    unit (polling stations) level and two-way cross-tabulated results at the district level.
    These data sets can be used to assess ecological inference algorithms devised 
    for estimating RxC (global) ecological contingency tables using exclusively aggregate results 
    from voting units.
    Reference:
    Pavía (2022) <doi:10.1177/08944393211040808>.
	"""
	
	cran = "ei.Datasets" 

	version("0.0.1-3", md5="ab99261013e5fad1305b663155095860")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
