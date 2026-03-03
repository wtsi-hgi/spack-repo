# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebiasinfer(RPackage):
	"""Efficient Inference on High-Dimensional Linear Model with
Missing Outcomes

	A statistically and computationally efficient debiasing method for conducting valid inference on the high-dimensional linear regression function with missing outcomes.
    The reference paper is Zhang, Giessing, and Chen (2023) <arXiv:2309.06429>. 
	"""
	
	homepage = "https://github.com/zhangyk8/Debias-Infer/"
	cran = "DebiasInfer" 

	version("0.2", md5="b61b7c23248e76dc84d3875f44c5a2e4")

	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
