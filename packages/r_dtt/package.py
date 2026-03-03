# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtt(RPackage):
	"""Discrete Trigonometric Transforms

	This package provides functions for 1D and 2D Discrete
        Cosine Transform (DCT), Discrete Sine Transform (DST) and
        Discrete Hartley Transform (DHT).
	"""
	
	homepage = "http://www.r-project.org"
	cran = "dtt" 

	version("0.1-2", md5="7707b3ca36465854b99e29729eefd50e")

