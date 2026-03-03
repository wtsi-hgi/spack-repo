# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorclustering(RPackage):
	"""Model-Based Tensor Clustering

	Performs model-based tensor clustering methods including Tensor Gaussian Mixture Model (TGMM), Tensor Envelope Mixture Model (TEMM) by Deng and Zhang (2021) <DOI: 10.1111/biom.13486>, Doubly-Enhanced EM (DEEM) algorithm by Mai, Zhang, Pan and Deng (2021) <DOI: 10.1080/01621459.2021.1904959>. 
	"""
	
	cran = "TensorClustering" 

	version("1.0.2", md5="7bed4b463613ef5a5dc15aadf3ddb8ef")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-tensr", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-tres", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
