# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZeroeqpart(RPackage):
	"""Zero Order vs (Semi) Partial Correlation Test and CI

	Uses bootstrap to test zero order correlation being equal to a 
    partial or semi-partial correlation (one or two tailed). Confidence 
    intervals for the parameter (zero order minus partial) can also be
    determined. Implements the bias-corrected and accelerated bootstrap
    method as described in "An Introduction to the Bootstrap" Efron (1983) 
    <0-412-04231-2>.
	"""
	
	homepage = "https://github.com/djrichar92/zeroEQpart"
	cran = "zeroEQpart" 

	version("0.1.0", md5="8d1967b45b6625b63672fa8811680e96")

	depends_on("r-ppcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
