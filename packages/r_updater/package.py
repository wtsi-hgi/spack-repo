# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpdater(RPackage):
	"""Utilities for Updating R

	When updating major or minor R versions all packages should
    be re-installed. The utilities in this package assist in getting a
    user up-and-running again by installing all previously installed R
    packages. The package uses 'renv' to install; immediately replenishing
    your 'renv' package cache.
	"""
	
	homepage = "https://github.com/ddsjoberg/updater"
	cran = "updater" 

	version("0.1.2", md5="225d69031248497702448d8b789e9f37")

	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-renv@1.0.2:", type=("build", "run"))
