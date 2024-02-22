# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvalysis(RPackage):
	"""Miscellaneous Functions for Environmental Analyses

	Small toolbox for data analyses in environmental chemistry and
    ecotoxicology. Provides, for example, calibration() to calculate calibration
    curves and corresponding limits of detection (LODs) and  limits of 
    quantification (LOQs) according to German DIN 32645 (2008). texture() makes
    it easy to estimate soil particle size distributions from hydrometer
    measurements (ASTM D422-63, 2007).
	"""
	
	homepage = "https://github.com/zsteinmetz/envalysis"
	cran = "envalysis" 

	version("0.6.0", md5="83b75d9cd54651bf2397d21fcfa66fbd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
