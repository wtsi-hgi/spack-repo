# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFledge(RPackage):
	"""Smoother Change Tracking and Versioning for R Packages

	Streamlines the process of updating changelogs (NEWS.md)
    and versioning R packages developed in git repositories.
	"""
	
	homepage = "https://fledge.cynkra.com/"
	cran = "fledge" 

	version("0.1.2", md5="0281f8563a0b31f16ddf60dee2ff5a61")

	depends_on("r-brio", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc@1.2:", type=("build", "run"))
	depends_on("r-gert@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rlang@0.4.12:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-usethis@1.5:", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
