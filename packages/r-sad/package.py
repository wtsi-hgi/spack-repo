# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSad(RPackage):
	"""Verify the Scale, Anisotropy and Direction of Weather Forecasts

	Implementation of the wavelet-based spatial verification method of Buschow and Friederichs "SAD: Verifying the Scale, Anisotropy and Direction of precipitation forecasts" (2020, submitted to QJRMS). Forecasts and Observations are transformed by a decimated or redundant dual-tree complex wavelet transform to analyze the spatial scale, degree of anisotropy and preferred direction in each field. These structural attributes are compared by a series of scores. An experimental algorithm for the correction of these errors is included as well.
	"""
	
	cran = "sad" 

	version("0.1.3", md5="1a64c20d0c76ce3b9f86cf6c2cce0377")

	depends_on("r-dualtrees", type=("build", "run"))
	depends_on("r-emdist", type=("build", "run"))
