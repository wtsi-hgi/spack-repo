# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscquartets(RPackage):
	"""Analyzing Gene Tree Quartets under the Multi-Species Coalescent

	Methods for analyzing and using quartets displayed on a collection 
 of gene trees, primarily to make inferences about the species tree or network 
 under the multi-species coalescent model. These include quartet hypothesis tests
 for the model, as developed by Mitchell et al. (2019) <doi:10.1214/19-EJS1576>, 
 simplex plots of quartet concordance factors as presented by Allman et al. (2020) 
 <doi:10.1101/2020.02.13.948083>, species tree inference methods based on quartet 
 distances of Rhodes (2019) <doi:10.1109/TCBB.2019.2917204> and Yourdkhani and 
 Rhodes (2019) <doi:10.1007/s11538-020-00773-4>, the NANUQ algorithm for inference 
 of level-1 species networks of Allman et al. (2019) <doi:10.1186/s13015-019-0159-2>, 
 and the TINNIK algorithm for inference of the tree of blobs of an arbitrary 
 network of Allman et al.(2022) <doi:10.1007/s00285-022-01838-9>. Software 
 announcement by Rhodes et al. (2020) <doi:10.1093/bioinformatics/btaa868>.
	"""
	
	cran = "MSCquartets" 

	version("2.0", md5="4fcbb02976a9b32c02b8036556e29738")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-zipfr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph@2:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
