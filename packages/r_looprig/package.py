# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLooprig(RPackage):
	"""Integration and Analysis of Chromatin Loop Data

	Common coordinate-based workflows involving processed chromatin loop and genomic element data are considered and packaged into appropriate customizable functions. Includes methods for linking element sets via chromatin loops and creating consensus loop datasets. 
	"""
	
	cran = "LoopRig" 

	version("0.1.1", md5="84ce7d790da54a1a436288b0aefbeb72")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
