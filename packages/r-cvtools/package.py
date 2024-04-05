# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvtools(RPackage):
	"""Cross-Validation Tools for Regression Models

	Tools that allow developers to write functions for
    cross-validation with minimal programming effort and assist
    users with model selection.
	"""
	
	cran = "cvTools" 

	version("0.3.3", md5="dea2e69a808ac8abbe6f902e17fc86ed")
	version("0.3.2", md5="df3f75920f5c2059ba9caee2c9a34067")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
