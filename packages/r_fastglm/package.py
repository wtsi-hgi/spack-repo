# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastglm(RPackage):
	"""Fast and Stable Fitting of Generalized Linear Models using
'RcppEigen'

	Fits generalized linear models efficiently using 'RcppEigen'. The iteratively reweighted least squares 
    implementation utilizes the step-halving approach of Marschner (2011) <doi:10.32614/RJ-2011-012> to help safeguard
    against convergence issues.
	"""
	
	cran = "fastglm" 

	version("0.0.3", md5="5268f76306dec9da5f000498ec01c3bd")

	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
