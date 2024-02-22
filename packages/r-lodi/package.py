# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLodi(RPackage):
	"""Limit of Detection Imputation for Single-Pollutant Models

	Impute observed values below the limit of detection (LOD) via
    censored likelihood multiple imputation (CLMI) in single-pollutant
    models, developed by Boss et al (2019) <doi:10.1097/EDE.0000000000001052>.
    CLMI handles exposure detection limits that may change throughout the course
    of exposure assessment. 'lodi' provides functions for imputing and
    pooling for this method.
	"""
	
	homepage = "https://github.com/umich-cphds/lodi"
	cran = "lodi" 

	version("0.9.2", md5="34423be9445fa3150a7d087d776e1f34")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
