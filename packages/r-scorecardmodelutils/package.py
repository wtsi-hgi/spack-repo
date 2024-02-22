# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScorecardmodelutils(RPackage):
	"""Credit Scorecard Modelling Utils

	Provides infrastructure functionalities such as missing value treatment, information value calculation, GINI calculation etc. which are used for developing a traditional credit scorecard as well as a machine learning based model. The functionalities defined are standard steps for any credit underwriting scorecard development, extensively used in financial domain.
	"""
	
	cran = "scorecardModelUtils" 

	version("0.0.1.0", md5="13aaabc9fa3a9879ddc2620db861d330")

	depends_on("r-car", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-gbm", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
