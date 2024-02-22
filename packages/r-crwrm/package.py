# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrwrm(RPackage):
	"""Changing the Reference Group without Re-Running the Model

	To re-calculate the coefficients and the standard deviation when changing the reference group.
	"""
	
	cran = "CRWRM" 

	version("0.0.1", md5="61d256b23c7767f0a7f15936e937ba16")

