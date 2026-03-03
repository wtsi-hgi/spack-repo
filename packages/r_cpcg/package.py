# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpcg(RPackage):
	"""Efficient and Customized Preconditioned Conjugate Gradient
Method for Solving System of Linear Equations

	Solves system of linear equations using (preconditioned) conjugate gradient algorithm, with improved efficiency using Armadillo templated 'C++' linear algebra library, and flexibility for user-specified preconditioning method. Please check <https://github.com/styvon/cPCG> for latest updates.
	"""
	
	cran = "cPCG" 

	version("1.0", md5="47f4ab9d920617d5cd298e44ef34ca83")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
