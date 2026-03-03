# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrandwatchr(RPackage):
	"""'Brandwatch' API to R

	Interact with the 'Brandwatch' API <https://developers.brandwatch.com/docs>. 
  Allows you to authenticate to the API and obtain data for projects, queries, query groups tags and categories.
  Also allows you to directly obtain mentions and aggregate data for a specified query or query group.
	"""
	
	homepage = "https://github.com/Phippsy/brandwatchR"
	cran = "brandwatchR" 

	version("0.3.0", md5="4f50f01ee3dada00999008c99e9070d3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
