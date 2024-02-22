# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrillr(RPackage):
	"""R Driver for Apache Drill

	Provides a R driver for Apache Drill<https://drill.apache.org>, which could connect to the Apache Drill cluster<https://drill.apache.org/docs/installing-drill-on-the-cluster> or drillbit<https://drill.apache.org/docs/embedded-mode-prerequisites> and get result(in data frame) from the SQL query and check the current configuration status. This link <https://drill.apache.org/docs> contains more information about Apache Drill.
	"""
	
	cran = "DrillR" 

	version("0.1", md5="9f8763c468302db548fcdc79c97d6179")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
