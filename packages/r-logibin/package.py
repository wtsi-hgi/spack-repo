# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogibin(RPackage):
	"""Binning Variables to Use in Logistic Regression

	Fast binning of multiple variables using parallel processing. A summary of all the variables binned is generated which provides the information value, entropy, an indicator of whether the variable follows a monotonic trend or not, etc. It supports rebinning of variables to force a monotonic trend as well as manual binning based on pre specified cuts. The cut points of the bins are based on conditional inference trees as implemented in the partykit package. The conditional inference framework is described by Hothorn T, Hornik K, Zeileis A (2006) <doi:10.1198/106186006X133933>.
	"""
	
	cran = "logiBin" 

	version("0.3", md5="7e7d203c8d97bb97d9fb04e972966836")

	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
