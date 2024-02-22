# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSohpie(RPackage):
	"""Statistical Approach via Pseudo-Value Information and Estimation

	'SOHPIE' (pronounced as SOFIE) is a novel pseudo-value regression approach for differential co-abundance network analysis of microbiome data, which can include additional clinical covariate in the model. The full methodological details can be found in Ahn S and Datta S (2023) <arXiv:2303.13702v1>.
	"""
	
	cran = "SOHPIE" 

	version("1.0.6", md5="7e10309df6cce675dfba9b1e9248b19c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
