# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsea(RPackage):
	"""Population-Specific Expression Analysis.

	Deconvolution of gene expression data by Population-Specific Expression Analysis (PSEA).
	"""
	
	bioc = "PSEA"

	version("1.36.0", commit="11e95fde4a6ea40858fda70cce20a9450543d67a")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
