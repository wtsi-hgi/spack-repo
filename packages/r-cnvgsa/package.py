# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvgsa(RPackage):
	"""Gene Set Analysis of (Rare) Copy Number Variants

	This package is intended to facilitate gene-set association with rare CNVs in case-control studies.
	"""
	
	bioc = "cnvGSA"

	version("1.52.0", commit="29c888e781219ebcadd75f3fe2051452cb181f15")
	version("1.46.0", commit="b1506807d5e6ec29fc4b269e28d41fb80f63875e")

	depends_on("r-brglm", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-splitstackshape", type=("build", "run"))
