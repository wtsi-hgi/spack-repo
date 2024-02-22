# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqest(RPackage):
	"""Sequential Method for Classification and Generalized Estimating
Equations Problem

	Sequential method to solve the the binary classification problem 
    by Wang (2019) <arXiv:arXiv:1901.10079>, multi-class 
    classification problem by Li (2020) <doi:10.1016/j.csda.2020.106911>
    and the highly stratified multiple-response problem by Chen (2019)
    <doi:10.1111/biom.13160>.
	"""
	
	cran = "seqest" 

	version("1.0.1", md5="4056f4f07e4fdfcefefc1ad9945c7f8b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-geepack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
