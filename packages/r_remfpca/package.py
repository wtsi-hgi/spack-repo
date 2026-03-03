# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemfpca(RPackage):
	"""Regularized Multivariate Functional Principal Component Analysis

	Methods and tools for implementing regularized multivariate functional principal component analysis ('ReMFPCA') for multivariate functional data whose variables might be observed over different dimensional domains. 'ReMFPCA' is an object-oriented interface leveraging the extensibility and scalability of R6. It employs a parameter vector to control the smoothness of each functional variable. By incorporating smoothness constraints as penalty terms within a regularized optimization framework, 'ReMFPCA' generates smooth multivariate functional principal components, offering a concise and interpretable representation of the data. For detailed information on the methods and techniques used in 'ReMFPCA', please refer to Haghbin et al. (2023) <doi:10.48550/arXiv.2306.13980>. 
	"""
	
	homepage = "https://github.com/haghbinh/ReMFPCA"
	cran = "ReMFPCA" 

	version("1.0.0", md5="5be4d0a15d274e1f60b3413b91867aea")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
