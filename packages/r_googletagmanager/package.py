# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogletagmanager(RPackage):
	"""Access the 'Google Tag Manager' API using R

	Interact with the 'Google Tag Manager' API <https://developers.google.com/tag-platform/tag-manager/api/v2>, enabling scripted deployments and updates across multiple tags, triggers, variables and containers. 
	"""
	
	cran = "googleTagManageR" 

	version("0.2.0", md5="f96071e770393554c6ad863d17c41f24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-future@1.2:", type=("build", "run"))
	depends_on("r-googleauthr@1.2.1:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
