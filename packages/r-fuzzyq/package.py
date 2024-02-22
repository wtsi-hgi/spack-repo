# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyq(RPackage):
	"""Fuzzy Quantification of Common and Rare Species

	Fuzzy clustering of species in an ecological community as common or
    rare based on their abundance and occupancy. It also includes functions to
    compute confidence intervals of classification metrics and plot results. See
    Balbuena et al. (2020, <doi:10.1101/2020.08.12.247502>).
	"""
	
	homepage = "https://ligophorus.github.io/FuzzyQ/"
	cran = "FuzzyQ" 

	version("0.1.0", md5="6656cb0153b2f85c300189e97385098c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
