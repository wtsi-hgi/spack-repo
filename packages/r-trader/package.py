# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrader(RPackage):
	"""Tree Ring Analysis of Disturbance Events in R

	Tree Ring Analysis of Disturbance Events in R (TRADER) package provides functions for disturbance reconstruction from tree-ring data, e.g. boundary line, absolute increase, growth averaging methods.
	"""
	
	homepage = "https://github.com/pavel-fibich/TRADER"
	cran = "TRADER" 

	version("1.2-4", md5="a0a86d481388450856764dbf89278286")

	depends_on("r-dplr", type=("build", "run"))
