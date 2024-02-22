# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackagediff(RPackage):
	"""Compare R Package Differences

	It provides utility functions for investigating changes within R
    packages. The pkgInfo() function extracts package information such as
    exported and non-exported functions as well as their arguments. The
    pkgDiff() function compares this information for two versions of a package
    and creates a diff file viewable in a browser.
	"""
	
	homepage = "https://github.com/couthcommander/packageDiff"
	cran = "packageDiff" 

	version("0.1", md5="8b230543aa51b0e8c4175882cd25c46b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-diffr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
