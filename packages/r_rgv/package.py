# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgv(RPackage):
	"""Analysis of Continuous Glucose Monitor Data

	Reads in continuous glucose monitor data of many different formats, calculates a host of glycemic variability metrics, and plots glucose over time. 
	"""
	
	cran = "rGV" 

	version("0.0.4", md5="4b4d07ab3efd56cd583cf9e096bcb128")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
