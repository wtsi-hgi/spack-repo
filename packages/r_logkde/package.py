# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogkde(RPackage):
	"""Computing Log-Transformed Kernel Density Estimates for Positive
Data

	Computes log-transformed kernel density estimates for positive data using a variety of kernels. It follows the methods described in Jones, Nguyen and McLachlan (2018) <doi:10.21105/joss.00870>.
	"""
	
	cran = "logKDE" 

	version("0.3.2", md5="140bfd90bb92e0ace15d766e0df2a69c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
