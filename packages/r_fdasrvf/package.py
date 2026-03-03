# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdasrvf(RPackage):
	"""Elastic Functional Data Analysis

	Performs alignment, PCA, and modeling of multidimensional and 
    unidimensional functions using the square-root velocity framework 
    (Srivastava et al., 2011 <arXiv:1103.3817> and Tucker et al., 2014 
    <DOI:10.1016/j.csda.2012.12.001>). This framework allows for elastic 
    analysis of functional data through phase and amplitude separation.
	"""
	
	homepage = "https://github.com/jdtuck/fdasrvf_R"
	cran = "fdasrvf" 

	version("2.2.0", md5="7a21fea14fb8995b322bd7065af5bae5")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tolerance", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
