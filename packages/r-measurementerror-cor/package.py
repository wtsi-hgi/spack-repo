# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasurementerrorCor(RPackage):
	"""Measurement Error model estimate for correlation coefficient

	Two-stage measurement error model for correlation estimation with smaller bias than the usual sample correlation
	"""
	
	bioc = "MeasurementError.cor"

	version("1.80.0", commit="bd585eb03cd521b5506f7a6374a365b42ca1ce79")
	version("1.74.0", commit="54fec2b2ec35cf2b2f6a67ddf9b2a22e38140418")

