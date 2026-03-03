# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpnmf(RPackage):
	"""Supervised NMF

	Non-negative Matrix Factorization(NMF) is a powerful tool for identifying the key features of microbial communities and a dimension-reduction method. When we are interested in the differences between the structures of two groups of communities, supervised NMF(Yun Cai, Hong Gu and Tobby Kenney (2017),<doi:10.1186/s40168-017-0323-1>) provides a better way to do this, while retaining all the advantages of NMF -- such as interpretability, and being based on a simple biological intuition.
	"""
	
	cran = "SpNMF" 

	version("0.1.1", md5="f59693aa9a902b42a8e287a8fd5e8f28")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
