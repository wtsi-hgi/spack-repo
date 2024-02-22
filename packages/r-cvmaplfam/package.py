# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvmaplfam(RPackage):
	"""Cross-Validation Model Averaging for Partial Linear Functional
Additive Models

	Produce an averaging estimate/prediction by combining all candidate models for partial linear functional additive models, 
    using multi-fold cross-validation criterion. More details can be referred to Shishi Liu and Jingxiao Zhang. (2021) <arXiv:2105.00966>.
	"""
	
	cran = "cvmaPLFAM" 

	version("0.1.0", md5="c4caa967acf698729cb727f7432544b9")

	depends_on("r-fda", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
