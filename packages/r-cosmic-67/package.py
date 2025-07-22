# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosmic67(RPackage):
	"""COSMIC.67

	COSMIC: Catalogue Of Somatic Mutations In Cancer, version 67 (2013-10-24)
	"""
	
	bioc = "COSMIC.67"

	version("1.44.0", commit="db83c1011b488a68828bda27fb07c0e53650aab2")
	version("1.38.0", md5="392f31ffd7e95a7558d248d36dcc37fe", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/COSMIC.67_1.38.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))

