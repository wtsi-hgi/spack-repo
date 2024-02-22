# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYatah(RPackage):
	"""Yet Another TAxonomy Handler

	Provides functions to manage taxonomy when lineages are
    described with strings and ranks separated with special patterns like
    "|*__" or ";*__".
	"""
	
	homepage = "https://abichat.github.io/yatah/"
	cran = "yatah" 

	version("0.2.1", md5="7d7c3f4865850d2ff9bc0f9a15d17c40")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
