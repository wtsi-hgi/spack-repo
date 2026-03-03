# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSprintr(RPackage):
	"""Sparse Reluctant Interaction Modeling

	An implementation of a computationally efficient method to fit large-scale interaction models based on the reluctant interaction selection principle. The method and its properties are described in greater depth in Yu, G., Bien, J., and Tibshirani, R.J. (2019) "Reluctant interaction modeling", which is available at <arXiv:1907.08414>.
	"""
	
	cran = "sprintr" 

	version("0.9.0", md5="82da44d6cb843e6677cff9891071aade")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
