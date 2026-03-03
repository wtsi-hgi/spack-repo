# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoconut(RPackage):
	"""COmbat CO-Normalization Using conTrols (COCONUT)

	Allows for pooled analysis of microarray data by batch-correcting control samples, and then applying the derived correction parameters to non-control samples to obtain bias-free, inter-dataset corrected data.
	"""
	
	cran = "COCONUT" 

	version("1.0.2", md5="14399abc50481cb7309b028cecd8e0f6")

