# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgetho(RPackage):
	"""Visualisation of High-Throughput Behavioural (i.e. Ethomics)
Data

	Extension of 'ggplot2' providing layers, scales and preprocessing functions
    useful to represent behavioural variables that are recorded over multiple animals and days.
    This package is part of the 'rethomics' framework <https://rethomics.github.io/>.
	"""
	
	homepage = "https://github.com/rethomics/ggetho"
	cran = "ggetho" 

	version("0.3.7", md5="f5d7f2aea7c2307d72b206dab317cb12")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-behavr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
