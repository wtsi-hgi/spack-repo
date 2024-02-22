# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RObssens(RPackage):
	"""Sensitivity Analysis for Observational Studies

	Observational studies are limited in that there could be an unmeasured variable related to both the response variable and the primary predictor.  If this unmeasured variable were included in the analysis it would change the relationship (possibly changing the conclusions).  Sensitivity analysis is a way to see how much of a relationship needs to exist with the unmeasured variable before the conclusions change.  This package provides tools for doing a sensitivity analysis for regression (linear, logistic, and cox) style models.
	"""
	
	cran = "obsSens" 

	version("1.4", md5="18018bd4a725e38eba111452ef1e11ab")

