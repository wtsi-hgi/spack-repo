# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighmlr(RPackage):
	"""Feature Selection for High Dimensional Survival Data

	Perform high dimensional Feature Selection in the presence of survival outcome.
            Based on Feature Selection method and different survival analysis, it will obtain the best 
            markers with optimal threshold levels according to their effect on disease progression
            and produce the most consistent level according to those threshold values. 
            The functions' methodology is based on by Sonabend et al (2021) <doi:10.1093/bioinformatics/btab039>  and Bhattacharjee  et al (2021) <arXiv:2012.02102>.
	"""
	
	cran = "highMLR" 

	version("0.1.1", md5="e1983c5b93c0471730477ffc398bfdf2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mlr3", type=("build", "run"))
	depends_on("r-mlr3learners", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-coxme", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
