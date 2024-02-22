# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNamer(RPackage):
	"""Names Your 'R Markdown' Chunks

	It names the 'R Markdown' chunks of files based on
    the filename.
	"""
	
	homepage = "https://github.com/jumpingrivers/namer"
	cran = "namer" 

	version("0.1.6", md5="e83835f7c3db8e4398b0943038b3e08d")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
