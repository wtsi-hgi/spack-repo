# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdarep(RPackage):
	"""Two-Dimensional FPCA, Marginal FPCA, and Product FPCA for
Repeated Functional Data

	Provides an implementation of two-dimensional functional principal component analysis (FPCA), Marginal FPCA, and Product FPCA for repeated functional data. Marginal and Product FPCA implementations are done for both dense and sparsely observed functional data. 
    References: Chen, K., Delicado, P., & Müller, H. G. (2017) <doi:10.1111/rssb.12160>.
                Chen, K., & Müller, H. G. (2012) <doi:10.1080/01621459.2012.734196>.
                Hall, P.,  Müller, H.G. and Wang, J.L. (2006) <doi:10.1214/009053606000000272>.
                Yao, F., Müller, H. G., & Wang, J. L. (2005) <doi:10.1198/016214504000001745>.
	"""
	
	homepage = "https://github.com/functionaldata/tFDArep"
	cran = "fdarep" 

	version("0.1.1", md5="30c90e4c1c75294156d58f0474879e5c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fdapace", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
