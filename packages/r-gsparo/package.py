# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsparo(RPackage):
	"""Group Sparse Optimization

	Approaches a group sparse solution of an underdetermined linear system. It implements the proximal gradient algorithm to solve a lower regularization model of group sparse learning. For details, please refer to the paper "Y. Hu, C. Li, K. Meng, J. Qin and X. Yang. Group sparse optimization via l_{p,q} regularization. Journal of Machine Learning Research, to appear, 2017".
	"""
	
	cran = "GSparO" 

	version("1.0", md5="9e2d6dcbe51f5479ff4c7cb04a212ea8")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-threeway", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
