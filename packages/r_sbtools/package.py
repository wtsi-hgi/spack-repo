# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbtools(RPackage):
	"""USGS ScienceBase Tools

	Tools for interacting with U.S. Geological Survey ScienceBase
    <https://www.sciencebase.gov> interfaces. ScienceBase is a data cataloging and
    collaborative data management platform. Functions included for querying
    ScienceBase, and creating and fetching datasets.
	"""
	
	homepage = "https://github.com/DOI-USGS/sbtools"
	cran = "sbtools" 

	version("1.3.2", md5="ccd3c8c5a8b2aaad2fd70a73834f744e")
	version("1.3.1", md5="f7bd3fbd5e1992796ea8e9bd9f23f9e2")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
