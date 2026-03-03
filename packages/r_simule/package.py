# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimule(RPackage):
	"""A Constrained L1 Minimization Approach for Estimating Multiple
Sparse Gaussian or Nonparanormal Graphical Models

	This is an R implementation of a constrained l1 minimization approach for estimating multiple Sparse Gaussian or Nonparanormal Graphical Models (SIMULE). The SIMULE algorithm can be used to estimate multiple related precision matrices. For instance, it can identify context-specific gene networks from multi-context gene expression datasets. By performing data-driven network inference from high-dimensional and heterogenous data sets, this tool can help users effectively translate aggregated data into knowledge that take the form of graphs among entities. Please run demo(simuleDemo) to learn the basic functions provided by this package. For further details, please read the original paper: Beilun Wang, Ritambhara Singh, Yanjun Qi (2017) <DOI:10.1007/s10994-017-5635-7>.
	"""
	
	homepage = "https://github.com/QData/SIMULE"
	cran = "simule" 

	version("1.3.0", md5="4cdc2fef3c55a700156f68171d795b76")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
