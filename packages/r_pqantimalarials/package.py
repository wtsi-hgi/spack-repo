# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPqantimalarials(RPackage):
	"""web tool for estimating under-five deaths caused by poor-quality
antimalarials in sub-Saharan Africa

	This package allows users to calculate the number of
    under-five child deaths caused by consumption of poor quality
    antimalarials across 39 sub-Saharan nations. The package supports one
    function, that starts an interactive web tool created using
    the shiny R package. The web tool runs locally on the user's machine.
    The web tool allows users to set input parameters (prevalence of poor
    quality antimalarials, case fatality rate of children who take poor
    quality antimalarials, and sample size) which are then used to perform
    an uncertainty analysis following the Latin hypercube
    sampling scheme. Users can download the output figures as PDFs, and the
    output data as CSVs. Users can also download their input parameters
    for reference. This package was designed to accompany the analysis
    presented in:
    J. Patrick Renschler, Kelsey Walters, Paul Newton, Ramanan Laxminarayan
    "Estimated under-five deaths associated with poor-quality
    antimalarials in sub-Saharan Africa", 2014. Paper submitted.
	"""
	
	cran = "pqantimalarials" 

	version("0.2", md5="451ae1daf8033dba141f8a60735655e4")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
