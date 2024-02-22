# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsibble(RPackage):
	"""Tidy Temporal Data Frames and Tools

	Provides a 'tbl_ts' class (the 'tsibble') for
    temporal data in an data- and model-oriented format. The 'tsibble'
    provides tools to easily manipulate and analyse temporal data, such as
    filling in time gaps and aggregating over calendar periods.
	"""
	
	homepage = "https://tsibble.tidyverts.org"
	cran = "tsibble" 

	version("1.1.4", md5="9e43ff1fa59c9385ba04a2bd04e04bbd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-anytime@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-ellipsis@0.3:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate@1.7:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-vctrs@0.3.1:", type=("build", "run"))
