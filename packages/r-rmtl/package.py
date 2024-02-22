# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmtl(RPackage):
	"""Regularized Multi-Task Learning

	Efficient solvers for 10 regularized multi-task learning algorithms applicable for regression, classification, joint feature selection, task clustering, low-rank learning, sparse learning and network incorporation. Based on the accelerated gradient descent method, the algorithms feature a state-of-art computational complexity O(1/k^2). Sparse model structure is induced by the solving the proximal operator. The detail of the package is described in the paper of Han Cao and Emanuel Schwarz (2018) <doi:10.1093/bioinformatics/bty831>.
	"""
	
	homepage = "https://github.com/transbioZI/RMTL/"
	cran = "RMTL" 

	version("0.9.9", md5="c4e28e076d1d323ee9a8313a4c833dd4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass@7.3.50:", type=("build", "run"))
	depends_on("r-psych@1.8.4:", type=("build", "run"))
	depends_on("r-corpcor@1.6.9:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
