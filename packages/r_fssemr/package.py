# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFssemr(RPackage):
	"""Fused Sparse Structural Equation Models to Jointly Infer Gene
Regulatory Network

	An optimizer of Fused-Sparse Structural Equation Models, which is 
 the state of the art jointly fused sparse maximum likelihood function 
 for structural equation models proposed by Xin Zhou and Xiaodong Cai (2018 
 <doi:10.1101/466623>).
	"""
	
	homepage = "https://github.com/Ivis4ml/fssemR"
	cran = "fssemR" 

	version("0.1.8", md5="dedf8f8210ed24d1954d586433032099")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
