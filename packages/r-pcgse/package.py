# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcgse(RPackage):
	"""Principal Component Gene Set Enrichment

	Contains logic for computing the statistical association of variable groups, i.e., gene sets, with respect to the principal components of genomic data.
	"""
	
	cran = "PCGSE" 

	version("0.5.0", md5="cdfe157e5625d567023ff8c626f456aa")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
