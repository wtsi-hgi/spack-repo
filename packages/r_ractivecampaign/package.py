# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRactivecampaign(RPackage):
	"""Loading Data from 'ActiveCampaign API v3'

	Interface for loading data from 'ActiveCampaign API v3' 
    <https://developers.activecampaign.com/reference>. Provide functions
    for getting data by deals, contacts, accounts, campaigns and messages.
	"""
	
	cran = "ractivecampaign" 

	version("0.2.0", md5="e180f6404659ac338bd0c15f5bdf917d")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-retry", type=("build", "run"))
