# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElgbd(RPackage):
	"""Empirical Likelihood for General Block Designs

	Performs hypothesis testing for general block designs with
    empirical likelihood. The core computational routines are implemented
    using the 'Eigen' 'C++' library and 'RcppEigen' interface, with
    'OpenMP' for parallel computation. Details of the methods are given in
    Kim, MacEachern, and Peruggia (2023)
    <doi:10.1080/10485252.2023.2206919>. This work was supported by the
    U.S. National Science Foundation under Grants No.  SES-1921523 and
    DMS-2015552.
	"""
	
	homepage = "https://github.com/markean/elgbd"
	cran = "elgbd" 

	version("0.9.0", md5="f6ca5ad3c780e0df2dc147d58eb91ad6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
