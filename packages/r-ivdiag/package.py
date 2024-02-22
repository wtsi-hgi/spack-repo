# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIvdiag(RPackage):
	"""Estimation and Diagnostic Tools for Instrumental Variables
Designs

	Estimation and diagnostic tools for instrumental variables designs, which implements the guidelines proposed in Lal et al. (2023) <arXiv:2303.11399>, including bootstrapped confidence intervals, effective F-statistic, Anderson-Rubin test, valid-t ratio test, and local-to-zero tests. 
	"""
	
	homepage = "https://yiqingxu.org/packages/ivDiag/"
	cran = "ivDiag" 

	version("1.0.6", md5="9485c5183db60cf683cd6e77d8acd975")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-lfe", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggfortify", type=("build", "run"))
	depends_on("r-wcorr", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
