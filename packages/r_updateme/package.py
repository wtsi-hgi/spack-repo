# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpdateme(RPackage):
	"""Informative Messages About Outdated Packages

	When a package is loaded, the source repository is checked for
    new versions and a message is shown in the console indicating whether the
    package is out of date.
	"""
	
	homepage = "https://github.com/wurli/updateme"
	cran = "updateme" 

	version("0.1.0", md5="4160f93f73c7a86abb4796a6ef60ca82")

	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
