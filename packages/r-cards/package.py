# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCards(RPackage):
	"""Analysis Results Data

	Construct Clinical Data Interchange Standards Consortium
    (CDISC) compliant Analysis Results Data objects. These objects are
    used and re-used to construct summary tables, visualizations, and
    written reports. The package also exports utilities for working with
    these objects and creating new Analysis Results Data objects.
	"""
	
	homepage = "https://github.com/insightsengineering/cards"
	cran = "cards" 

	version("0.1.0", md5="7b3ac6df9be90aec326b8121b9b814be")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
