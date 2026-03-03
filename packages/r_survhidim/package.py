# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvhidim(RPackage):
	"""High Dimensional Survival Data Analysis

	High dimensional time to events data analysis with variable selection technique.
             Currently support LASSO, clustering and Bonferroni's correction.
	"""
	
	cran = "SurvHiDim" 

	version("0.1.1", md5="c061cd24e2be05173f784f2e333d8fc9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-useful", type=("build", "run"))
