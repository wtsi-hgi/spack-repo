# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFetchsalesforcer(RPackage):
	"""Get Data from Salesforce via the 'Windsor.ai' API

	Collect  your data on digital marketing campaigns from Salesforce using the 'Windsor.ai' API <https://windsor.ai/api-fields/>.
	"""
	
	homepage = "https://windsor.ai/"
	cran = "fetchSalesforceR" 

	version("0.1.0", md5="7eb97d83dc4e07c2fce1d170be1264ea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.2:", type=("build", "run"))
