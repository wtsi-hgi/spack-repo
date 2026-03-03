# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsyphy(RPackage):
	"""Functions for Analyzing Psychophysical Data in R

	An assortment of functions that could be useful in analyzing data from psychophysical experiments. It includes functions for calculating d' from several different experimental designs, links for m-alternative forced-choice (mafc) data to be used with the binomial family in glm (and possibly other contexts) and self-Start functions for estimating gamma values for CRT screen calibrations.
	"""
	
	cran = "psyphy" 

	version("0.3", md5="9d0765d3d70ddb010ad5f9f712a08b54")

	depends_on("r@3:", type=("build", "run"))
