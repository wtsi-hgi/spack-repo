# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrocran(RPackage):
	"""Hosting an Independent CRAN Repository

	Stand-alone HTTP capable R-package repository,
    that fully supports R's install.packages() and available.packages().
    It also contains API endpoints for end-users to add/update packages.
    This package can supplement 'miniCRAN', which has functions for maintaining
    a local (partial) copy of 'CRAN'.
    Current version is bare-minimum without any access-control or much security.
	"""
	
	cran = "microCRAN" 

	version("0.9.0-1", md5="23955b6877bd81eb4b07c6fcf7f03afb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-plumber@1.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
