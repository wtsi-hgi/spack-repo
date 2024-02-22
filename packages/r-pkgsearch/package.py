# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgsearch(RPackage):
	"""Search and Query CRAN R Packages

	Search CRAN metadata about packages by keyword, popularity,
    recent activity, package name and more. Uses the 'R-hub' search
    server, see <https://r-pkg.org> and the CRAN metadata database, that
    contains information about CRAN packages. Note that this is _not_ a
    CRAN project.
	"""
	
	homepage = "https://github.com/r-hub/pkgsearch"
	cran = "pkgsearch" 

	version("3.1.3", md5="5506c33a6c44075c92b56d27eb68aabf")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
