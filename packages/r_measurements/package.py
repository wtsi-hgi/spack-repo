# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasurements(RPackage):
	"""Tools for Units of Measurement

	Collection of tools to make working with physical measurements
		easier. Convert between metric and imperial units, or calculate a dimension's
		unknown value from other dimensions' measurements.
	"""
	
	cran = "measurements" 

	version("1.5.1", md5="ddeca3a4c7c46c10a4b175bccbcca2de")

