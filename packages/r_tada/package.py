# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTada(RPackage):
	"""Supporting Tools for Tada Science

	Suite of tools to support the practice of tada science. It includes an
    engaging package roulette that is designed to facilitate learning about 
    new packages. 
	"""
	
	homepage = "https://github.com/tadascience/tada"
	cran = "tada" 

	version("2024.1.0", md5="9ef225ca6736b0873c1b57d52624cff5")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
