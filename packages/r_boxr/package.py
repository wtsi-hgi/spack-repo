# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoxr(RPackage):
	"""Interface for the 'Box.com API'

	An R interface for the remote file hosting service 'Box'
    (<https://www.box.com/>). In addition to uploading and downloading files,
    this package includes functions which mirror base R operations for local
    files, (e.g. box_load(), box_save(), box_read(), box_setwd(), etc.), as well
    as 'git' style functions for entire directories (e.g. box_fetch(),
    box_push()).
	"""
	
	homepage = "https://github.com/r-box/boxr/"
	cran = "boxr" 

	version("0.3.6", md5="d7a823a3d2f1aafe68bc560cff1ceb59")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
