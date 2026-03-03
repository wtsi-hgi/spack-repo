# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfl(RPackage):
	"""Linguistic Fuzzy Logic

	Various algorithms related to linguistic fuzzy logic: mining for linguistic fuzzy association
    rules, composition of fuzzy relations, performing perception-based logical deduction (PbLD), 
    and forecasting time-series using fuzzy rule-based ensemble (FRBE). The package also contains basic
    fuzzy-related algebraic functions capable of handling missing values in different styles (Bochvar,
    Sobocinski, Kleene etc.), computation of Sugeno integrals and fuzzy transform.
	"""
	
	cran = "lfl" 

	version("2.2.0", md5="a073833815a6704c7340c0181e0ed466")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-forecast@5.5:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
