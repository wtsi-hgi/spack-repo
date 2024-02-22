# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfutilities(RPackage):
	"""Random Forests Model Selection and Performance Evaluation

	Utilities for Random Forest model selection, class balance
    correction, significance test, cross validation and partial dependency
    plots.
	"""
	
	homepage = "https://github.com/jeffreyevans/rfUtilities"
	cran = "rfUtilities" 

	version("2.1-5", md5="1aa7d04edca1284fe4d025d730d4a21e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-randomforest@4.6.12:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
