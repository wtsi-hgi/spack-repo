# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelf(RPackage):
	"""A Structural Equation Embedded Likelihood Framework for Causal
Discovery

	Provides the SELF criteria to learn causal structure. Please cite "Ruichu Cai, Jie Qiao, Zhenjie Zhang, Zhifeng Hao. SELF: Structural Equational Embedded Likelihood Framework for Causal Discovery. AAAI. 2018."
	"""
	
	cran = "SELF" 

	version("0.1.1", md5="9f42a12db381a24774744722005bf576")

	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-xgboost@0.6.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-comparecausalnetworks@0.1:", type=("build", "run"))
	depends_on("r-bnlearn@4.1.1:", type=("build", "run"))
