# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMds(RPackage):
	"""Medical Devices Surveillance

	A set of core functions for handling medical device event data in
    the context of post-market surveillance, pharmacovigilance, signal detection
    and trending, and regulatory reporting. Primary inputs are data on events by
    device and data on exposures by device. Outputs include: standardized
    device-event and exposure datasets, defined analyses, and time series.
	"""
	
	cran = "mds" 

	version("0.3.2", md5="598e1c8e63803605466a5315d4108d76")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-parsedate", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
