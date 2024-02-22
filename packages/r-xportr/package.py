# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXportr(RPackage):
	"""Utilities to Output CDISC SDTM/ADaM XPT Files

	Tools to build CDISC compliant data sets and check for CDISC compliance.
	"""
	
	homepage = "https://github.com/atorus-research/xportr"
	cran = "xportr" 

	version("0.3.2", md5="9de9aea1fc9cddeb8d497449d1a5b739")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-haven@2.5:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
