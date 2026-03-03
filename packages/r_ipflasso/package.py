# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpflasso(RPackage):
	"""Integrative Lasso with Penalty Factors

	The core of the package is cvr2.ipflasso(), an extension of glmnet to be used when the (large) set of available predictors is partitioned into several modalities which potentially differ with respect to their information content in terms of prediction. For example, in biomedical applications patient outcome such as survival time or response to therapy may have to be predicted based on, say, mRNA data, miRNA data, methylation data, CNV data, clinical data, etc. The clinical predictors are on average often much more important for outcome prediction than the mRNA data. The ipflasso method takes this problem into account by using different penalty parameters for predictors from different modalities. The ratio between the different penalty parameters can be chosen from a set of optional candidates by cross-validation or alternatively generated from the input data.
	"""
	
	cran = "ipflasso" 

	version("1.1", md5="5347fced730ec2b92709b71239da7188")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
