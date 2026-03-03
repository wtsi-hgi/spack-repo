# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTplyr(RPackage):
	"""A Traceability Focused Grammar of Clinical Data Summary

	A traceability focused tool created to simplify the data manipulation necessary to create clinical summaries.
	"""
	
	homepage = "https://github.com/atorus-research/Tplyr"
	cran = "Tplyr" 

	version("1.2.1", md5="67f8e242148b434d3d729624a1caac52")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
