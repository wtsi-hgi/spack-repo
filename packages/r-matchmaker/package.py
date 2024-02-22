# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatchmaker(RPackage):
	"""Flexible Dictionary-Based Cleaning

	Provides flexible dictionary-based
    cleaning that allows users to specify implicit and explicit missing data,
    regular expressions for both data and columns, and global matches, while
    respecting ordering of factors. This package is part of the 'RECON'
    (<https://www.repidemicsconsortium.org/>) toolkit for outbreak analysis.
	"""
	
	homepage = "https://www.repidemicsconsortium.org/matchmaker"
	cran = "matchmaker" 

	version("0.1.1", md5="e0fcb8773588fa7affe29ea696bc2611")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
