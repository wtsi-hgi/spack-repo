# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltaplotr(RPackage):
	"""Identification of Dichotomous Differential Item Functioning
(DIF) using Angoff's Delta Plot Method

	The deltaPlotR package implements Angoff's Delta Plot method to detect dichotomous DIF. Several detection thresholds are included, either from multivariate normality assumption or by prior determination. Item purification is supported (Magis and Facon (2014) <doi:10.18637/jss.v059.c01>).
	"""
	
	cran = "deltaPlotR" 

	version("1.6", md5="099946605bcef2922f5db863381dc90f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
