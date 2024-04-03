# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCardx(RPackage):
	"""Extra Analysis Results Data Utilities

	Create extra Analysis Results Data (ARD) summary objects.
    The package supplements the simple ARD functions from the 'cards'
    package, exporting functions to put statistical results in the ARD
    format. These objects are used and re-used to construct summary
    tables, visualizations, and written reports.
	"""
	
	homepage = "https://github.com/insightsengineering/cardx"
	cran = "cardx" 

	version("0.1.0", md5="643cb467593ea5b1b7028e0d229a5c71")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cards@0.1:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
