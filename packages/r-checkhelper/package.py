# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheckhelper(RPackage):
	"""Deal with Check Outputs

	Deal with packages 'check' outputs and reduce the risk of
    rejection by 'CRAN' by following policies.
	"""
	
	homepage = "https://thinkr-open.github.io/checkhelper/"
	cran = "checkhelper" 

	version("0.1.1", md5="8cecc3693833d15d781f4fcda91a8e1a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcmdcheck", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-whisker@0.4:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
