# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcesvms(RPackage):
	"""Link to the ICES Vessel Monitoring System and Logbook Database
Web Services

	Links to the ICES Vessel Monitoring System (VMS) and logbook database web services 
  <https://data.ices.dk/vms/webservices> to allow users to download summaries and data products.
	"""
	
	homepage = "https://data.ices.dk/vms"
	cran = "icesVMS" 

	version("1.1.4", md5="9ffedd06fec9edab43c5cd55964e8e49")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-icesconnect@1:", type=("build", "run"))
	depends_on("r-icesvocab", type=("build", "run"))
