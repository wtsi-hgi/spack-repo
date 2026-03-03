# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemcal(RPackage):
	"""Calibration Functions for Analytical Chemistry

	Simple functions for plotting linear
	calibration functions and estimating standard errors for measurements
	according to the Handbook of Chemometrics and Qualimetrics: Part A
	by Massart et al. (1997) There are also functions estimating the limit
	of detection (LOD) and limit of quantification (LOQ).
	The functions work on model objects from - optionally weighted - linear
	regression (lm) or robust linear regression ('rlm' from the 'MASS' package).
	"""
	
	homepage = "https://pkgdown.jrwb.de/chemCal/"
	cran = "chemCal" 

	version("0.2.3", md5="2e09ff875fc01d0219c8d58f54144d9a")

