# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepnorm(RPackage):
	"""Stepwise normalization functions for cDNA microarrays

	Stepwise normalization functions for cDNA microarray data.
	"""
	
	homepage = "http://www.biostat.ucsf.edu/jean/"
	bioc = "stepNorm"

	version("1.80.0", commit="cc3b995c06658635a448064a728a2d120588ad6a")
	version("1.74.0", commit="f7acc23850c2812f7de8dec96253be2163804080")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
