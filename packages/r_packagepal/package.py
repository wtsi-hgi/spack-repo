# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackagepal(RPackage):
	"""Guidelines and Checklists for Building CRAN-Worthy Packages

	Provides essential checklists for R package developers, whether
    you're creating your first package or beginning a new project. This tool
    guides you through each step of the development process, including specific
    considerations for submitting your package to the Comprehensive R Archive
    Network (CRAN). Simplify your workflow and ensure adherence to best
    practices with 'packagepal'.
	"""
	
	homepage = "https://github.com/lddurbin/packagepal"
	cran = "packagepal" 

	version("0.1.0", md5="e3390494b3c301b0fb02f46291682e61")

	depends_on("r-available@1.1:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-usethis@2.2.2:", type=("build", "run"))
