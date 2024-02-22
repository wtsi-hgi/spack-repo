# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCache(RPackage):
	"""Cache and Retrieve Computation Results

	Easily cache and retrieve computation results. The package works seamlessly across interactive R sessions, R scripts and Rmarkdown documents.
	"""
	
	homepage = "https://github.com/OlivierBinette/cache"
	cran = "cache" 

	version("0.0.3", md5="b2f35459eb8b8d4ed4716233a9d84072")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-assert", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
