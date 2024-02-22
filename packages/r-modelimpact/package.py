# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelimpact(RPackage):
	"""Functions to Assess the Business Impact of Churn Prediction
Models

	Calculate the financial impact of using a churn model in terms of cost, revenue, profit and return on investment.
	"""
	
	homepage = "https://github.com/PeerChristensen/modelimpact"
	cran = "modelimpact" 

	version("1.0.0", md5="d49f81dc5d06b0154f1833a1fbf69d0a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
