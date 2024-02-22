# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBingroup2(RPackage):
	"""Identification and Estimation using Group Testing

	Methods for the group testing identification problem: 1) Operating 
    characteristics (e.g., expected number of tests) for commonly used 
    hierarchical and array-based algorithms, and 2) Optimal testing 
    configurations for these same algorithms. Methods for the group testing 
    estimation problem: 1) Estimation and inference procedures for an overall 
    prevalence, and 2) Regression modeling for commonly used hierarchical and 
    array-based algorithms. 
	"""
	
	cran = "binGroup2" 

	version("1.3.1", md5="7d64c1c0320c4863f780a59f03faadfc", url="https://cran.r-project.org/src/contrib/binGroup2_1.3.1.tar.gz")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-partitions", type=("build", "run"))
	depends_on("r-rbeta2009", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
