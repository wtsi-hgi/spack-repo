# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFi(RPackage):
	"""Provide functions for forest inventory calculations

	Provide functions for forest inventory calculations.
        Common volumetric equations (Smalian, Newton and Huber) as well
        stacking factor and form
	"""
	
	cran = "FI" 

	version("1.0", md5="f941c37d75c7d780b61c4dc1ddff6b2b")

