# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComf(RPackage):
	"""Models and Equations for Human Comfort Research

	Calculation of various common and less common comfort indices such as predicted mean vote or the two node model. Converts physical variables such as relative to absolute humidity and evaluates the performance of comfort indices.
	"""
	
	cran = "comf" 

	version("0.1.12", md5="dcbd5df807792cc21e2738656d835419")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
