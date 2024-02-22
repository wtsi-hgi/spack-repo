# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROscv(RPackage):
	"""One-Sided Cross-Validation

	Functions for implementing different versions of the OSCV method in the kernel regression and density estimation frameworks. The package mainly supports the following articles: (1) Savchuk, O.Y., Hart, J.D. (2017). Fully robust one-sided cross-validation for regression functions. Computational Statistics, <doi:10.1007/s00180-017-0713-7> and (2) Savchuk, O.Y. (2017). One-sided cross-validation for nonsmooth density functions, <arXiv:1703.05157>.
	"""
	
	cran = "OSCV" 

	version("1.0", md5="e137bbbfd5497ab1bd95c33ccd6e4fbc")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-mc2d", type=("build", "run"))
