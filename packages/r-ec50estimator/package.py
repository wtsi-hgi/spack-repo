# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REc50estimator(RPackage):
	"""An Automated Way to Estimate EC50 for Stratified Datasets

	An implementation for estimating Effective control to 50% of growth
    inhibition (EC50) for multi isolates and stratified datasets. It implements 
    functions from the drc package in a way that is displayed a tidy data.frame 
    as output. Info about the drc package is available in Ritz C, Baty F, Streibig JC,
    Gerhard D (2015) <doi:10.1371/journal.pone.0146021>.
	"""
	
	homepage = "https://github.com/AlvesKS/ec50estimator"
	cran = "ec50estimator" 

	version("0.1.0", md5="732eee75aec154d47f78b75ef491cc72")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
