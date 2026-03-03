# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompindpca(RPackage):
	"""Computation of Relative Weights of Variables and Composite Index
Values Based on PCA

	It helps in development of a principal component analysis based composite index by assigning weights to variables and combining the weighted variables. For method details see Sendhil, R., Jha, A., Kumar, A. and Singh, S. (2018). <doi:10.1016/j.ecolind.2018.02.053>, and Wu, T. (2021). <doi:10.1016/j.ecolind.2021.108006>.
	"""
	
	cran = "compindPCA" 

	version("0.1.0", md5="6f83f5641399dcb9e72259e306bc95ed")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
