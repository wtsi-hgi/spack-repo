# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmptzcurve(RPackage):
	"""Gompertz Curve Fitting

	A system for fitting Gompertz Curve in a Time Series Data.
	"""
	
	cran = "GmptzCurve" 

	version("0.1.0", md5="d439e1c825d7b0a3730760cfd4db5b33")

