# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemver(RPackage):
	"""'Semantic Versioning V2.0.0' Parser

	Tools and functions for parsing, rendering and operating on
    semantic version strings. Semantic versioning is a simple set of rules
    and requirements that dictate how version numbers are assigned and
    incremented as outlined at <http://semver.org>.
	"""
	
	homepage = "https://github.com/johndharrison/semver"
	cran = "semver" 

	version("0.2.0", md5="35099b273e44874fd7561473f292ac11")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
