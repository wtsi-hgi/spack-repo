# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcbr(RPackage):
	"""Random Coefficient Binary Response Estimation

	Nonparametric maximum likelihood estimation methods
    for random coefficient binary response  models and some related
    functionality for sequential processing of hyperplane arrangements.
    See J. Gu and R. Koenker (2020) <DOI:10.1080/01621459.2020.1802284>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "RCBR" 

	version("0.6.2", md5="9384b4f58e7bef0301736ecdf59c08ef")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmosek", type=("build", "run"))
	depends_on("r-rebayes", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
