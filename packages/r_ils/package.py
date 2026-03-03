# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIls(RPackage):
	"""Interlaboratory Study

	It performs interlaboratory studies (ILS) to detect those
    laboratories that provide non-consistent results when comparing to others. It
    permits to work simultaneously with various testing materials, from standard
    univariate, and functional data analysis (FDA) perspectives. The univariate
    approach based on ASTM E691-08 consist of estimating the Mandel's h and
    k statistics to identify those laboratories that provide more significant
    different results, testing also the presence of outliers by Cochran and Grubbs
    tests, Analysis of variance (ANOVA) techniques are provided (F and Tuckey
    tests) to test differences in means corresponding to different laboratories per
    each material. Taking into account the functional nature of data retrieved in
    analytical chemistry, applied physics and engineering (spectra, thermograms,
    etc.). ILS package provides a FDA approach for finding the Mandel's k and h
    statistics distribution by smoothing bootstrap resampling.
	"""
	
	homepage = "https://github.com/mflores72000/ILS/"
	cran = "ILS" 

	version("0.3", md5="95e808b85a5a48b4c9f368572f7a2590")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-depthtools", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
