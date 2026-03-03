# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDunlin(RPackage):
	"""Preprocessing Tools for Clinical Trial Data

	A collection of functions to preprocess data and organize
    them in a format amenable to use by chevron.
	"""
	
	homepage = "https://insightsengineering.github.io/dunlin/"
	cran = "dunlin" 

	version("0.1.7", md5="0f317065ecfe7c11f5b64d1e8b065112")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-forcats@1:", type=("build", "run"))
	depends_on("r-glue@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-yaml@2.1.15:", type=("build", "run"))
