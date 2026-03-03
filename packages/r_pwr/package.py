# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwr(RPackage):
	"""Basic Functions for Power Analysis

	Power analysis functions along the lines of Cohen (1988).
	"""
	
	homepage = "https://github.com/heliosdrm/pwr"
	cran = "pwr" 

	version("1.3-0", md5="8855e45d6dabfa18015f97bda4b40547")

