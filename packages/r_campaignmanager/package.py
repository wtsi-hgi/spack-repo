# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCampaignmanager(RPackage):
	"""Connect to Campaign Manager via the 'Windsor.ai' API

	Collect  marketing data from Campaign Manager using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "campaignmanageR" 

	version("0.1.0", md5="eeeb5a38549bb79770c1b0c56af6051b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
