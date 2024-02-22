# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROner(RPackage):
	"""One Rule Machine Learning Classification Algorithm with
Enhancements

	Implements the One Rule (OneR) Machine Learning classification algorithm (Holte, R.C. (1993) <doi:10.1023/A:1022631118932>) with enhancements for sophisticated handling of numeric data and missing values together with extensive diagnostic functions. It is useful as a baseline for machine learning models and the rules are often helpful heuristics.
	"""
	
	homepage = "https://github.com/vonjd/OneR"
	cran = "OneR" 

	version("2.2", md5="55d34a060ae6ecf42711aaa5cc5945cd")

	depends_on("r@2.10:", type=("build", "run"))
