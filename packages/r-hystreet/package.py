# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHystreet(RPackage):
	"""Get Pedestrian Frequency Data from the 'Hystreet' Project

	An R API wrapper for the 'Hystreet' project <https://hystreet.com>. 'Hystreet' provides pedestrian counts in different cities in Germany.
	"""
	
	homepage = "https://github.com/JohannesFriedrich/hystReet"
	cran = "hystReet" 

	version("0.0.3", md5="cc194a87b3c025600f7a45c4414ffcbc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
