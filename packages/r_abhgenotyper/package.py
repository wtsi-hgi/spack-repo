# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbhgenotyper(RPackage):
	"""Easy Visualization of ABH Genotypes

	Easy to use functions to visualize marker data
    from biparental populations. Useful for both analyzing and
    presenting genotypes in the ABH format.
	"""
	
	homepage = "http://github.com/StefanReuscher/ABHgenotypeR"
	cran = "ABHgenotypeR" 

	version("1.0.1", md5="ca4397ba7390c0e0a3728c0cda864494")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
