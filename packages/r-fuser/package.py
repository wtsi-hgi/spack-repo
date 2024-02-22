# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuser(RPackage):
	"""Fused Lasso for High-Dimensional Regression over Groups

	Enables high-dimensional penalized regression across heterogeneous 
    subgroups. Fusion penalties are used to share information about the linear 
    parameters across subgroups. The underlying model is described 
    in detail in Dondelinger and Mukherjee (2017) <arXiv:1611.00953>.
	"""
	
	cran = "fuser" 

	version("1.0.1", md5="3017fa01788ca9e7956c4ad34ef006af")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
