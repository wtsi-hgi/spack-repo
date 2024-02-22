# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixtwice(RPackage):
	"""Large-Scale Hypothesis Testing by Variance Mixing

	Implements large-scale hypothesis testing by variance mixing. It takes two statistics per testing unit -- an estimated effect and its associated squared standard error -- and fits a nonparametric, shape-constrained mixture separately on two latent parameters. It reports local false discovery rates (lfdr) and local false sign rates (lfsr). Manuscript describing algorithm of MixTwice: Zheng et al(2021) <doi: 10.1093/bioinformatics/btab162>.
	"""
	
	cran = "MixTwice" 

	version("2.0", md5="9affd181eee7e96fd77d40e1c2f9a9b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-alabama", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
