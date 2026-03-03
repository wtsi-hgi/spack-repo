# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbedrock(RPackage):
	"""Analysis and Manipulation of Data from Minecraft Bedrock Edition

	Implements an interface to Minecraft (Bedrock Edition) worlds. Supports the analysis and management of these worlds and game saves.
	"""
	
	homepage = "https://github.com/reedacartwright/rbedrock"
	cran = "rbedrock" 

	version("0.3.2", md5="dd85b98b0e60f2e5765a7469b5a61eff")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("cmake", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
