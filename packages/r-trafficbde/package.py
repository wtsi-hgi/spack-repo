# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrafficbde(RPackage):
	"""Traffic Predictions Using Neural Networks

	Estimate and return either the traffic speed or the car entries in the city of Thessaloniki using historical traffic data. It's used in transport pilot of the 'BigDataEurope' project. There are functions for processing these data, training a neural network, select the most appropriate model and predict the traffic speed or the car entries for a selected time date.
	"""
	
	homepage = "https://github.com/okgreece/TrafficBDE"
	cran = "TrafficBDE" 

	version("0.1.2", md5="e73b1e8724c62bd019e639981f4cfd40")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-descriptivestats-obeu", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
