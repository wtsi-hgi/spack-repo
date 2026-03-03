# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfinterpret(RPackage):
	"""Descriptive Interpretations of Confidence Intervals

	Produces descriptive interpretations of confidence intervals.
    Includes (extensible) support for various test types, specified as sets
    of interpretations dependent on where the lower and upper confidence limits
    sit. Provides plotting functions for graphical display of interpretations.
	"""
	
	homepage = "https://github.com/jimvine/confinterpret"
	cran = "confinterpret" 

	version("1.0.0", md5="bcd4b1e02c0889eab8c4fd6794cef187")

