# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaptanr(RPackage):
	"""Call the 'NaPTAN' API Through R

	An R wrapper for pulling data from the National Public Transport Access Nodes ('NaPTAN') API (<https://www.api.gov.uk/dft/national-public-transport-access-nodes-naptan-api/#national-public-transport-access-nodes-naptan-api>). This allows users to download 'NaPTAN' transport information, for the full dataset, by ATCO region code, or by name of region.  
	"""
	
	cran = "naptanr" 

	version("1.0.1", md5="591c09cba5adf9da365debaacc9a2683")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
