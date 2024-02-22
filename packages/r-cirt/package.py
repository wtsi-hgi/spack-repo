# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCirt(RPackage):
	"""Choice Item Response Theory

	Jointly model the accuracy of cognitive responses and item choices
    within a Bayesian hierarchical framework as described by Culpepper and
    Balamuta (2015) <doi:10.1007/s11336-015-9484-7>. In addition, the package
    contains the datasets used within the analysis of the paper.
	"""
	
	homepage = "https://tmsalab.github.io/cIRT/"
	cran = "cIRT" 

	version("1.3.2", md5="5ca2aeb2ae0b3dfbfd14e7732425725f")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.8.1:", type=("build", "run"))
