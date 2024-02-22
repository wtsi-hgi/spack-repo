# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassivegst(RPackage):
	"""Competitive Gene Sets Test with the Mann-Whitney-Wilcoxon Test

	Friendly implementation of the Mann-Whitney-Wilcoxon test for competitive gene set enrichment analysis.
	"""
	
	homepage = "<https://github.com/stefanoMP/massiveGST>"
	cran = "massiveGST" 

	version("1.2.3", md5="7575750d57640bd41f3f6a3c7bda0dab")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-formattable@0.2.1:", type=("build", "run"))
	depends_on("r-msigdbr@7.4:", type=("build", "run"))
	depends_on("r-writexls@6.3:", type=("build", "run"))
	depends_on("r-igraph@1.2.6:", type=("build", "run"))
	depends_on("r-visnetwork@2.0.9:", type=("build", "run"))
