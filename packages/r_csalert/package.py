# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsalert(RPackage):
	"""Alerts from Public Health Surveillance Data

	Helps create alerts and determine trends by using various methods to analyze public health surveillance data. The primary analysis method is based upon a published analytics strategy by Benedetti (2019) <doi:10.5588/pha.19.0002>.
	"""
	
	homepage = "https://www.csids.no/csalert/"
	cran = "csalert" 

	version("2023.6.17", md5="ad5bc5a35847b9f76d0375cfa922096e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-cstidy", type=("build", "run"))
	depends_on("r-cstime", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
