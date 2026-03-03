# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgverse(RPackage):
	"""Build a Meta-Package Universe

	Build your own universe of packages similar to the 'tidyverse'
    package <https://tidyverse.org/> with this meta-package creator. Create a
    package-verse, or meta package, by supplying a custom name for the
    collection of packages and the vector of desired package names to include–
    and optionally supply a destination directory, an indicator of whether to
    keep the created package directory, and/or a vector of verbs implement via
    the 'usethis' <http://usethis.r-lib.org/> package.
	"""
	
	homepage = "https://pkgverse.mikewk.com"
	cran = "pkgverse" 

	version("0.0.1", md5="3cda9fa8e829ac2239433fb5f063667a")

	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
