# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsurvey(RPackage):
	"""Constrained Regression for Survey Data

	Domain mean estimation with monotonicity or block monotone constraints. See Xu X, Meyer MC and Opsomer JD (2021)<doi:10.1016/j.jspi.2021.02.004> for more details. 
	"""
	
	cran = "csurvey" 

	version("1.9", md5="382aff90299e2eea3b50536472d7a9af")

	depends_on("r-survey@4.2.1:", type=("build", "run"))
	depends_on("r-cgam@1.7:", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-coneproj", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
