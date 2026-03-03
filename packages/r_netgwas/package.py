# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetgwas(RPackage):
	"""Network-Based Genome Wide Association Studies

	A multi-core R package that contains a set of tools based on copula graphical
             models for accomplishing the three interrelated goals in genetics and genomics in an
			 unified way: (1) linkage map construction, (2) constructing linkage disequilibrium
			 networks, and (3) exploring high-dimensional genotype-phenotype network and genotype-
			 phenotype-environment interactions networks. 
			 The 'netgwas' package can deal with biparental inbreeding and outbreeding species with
			 any ploidy level, namely diploid (2 sets of chromosomes), triploid (3 sets of chromosomes),
			 tetraploid (4 sets of chromosomes) and so on. We target on high-dimensional data where 
			 number of variables p is considerably larger than number of sample sizes (p >> n). 
			 The computations is memory-optimized using the sparse matrix output. The 'netgwas' 
			 implements the methodological developments in Behrouzi and Wit (2017)
             <doi:10.1111/rssc.12287> and Behrouzi and Wit (2017) <doi:10.1093/bioinformatics/bty777>. 
	"""
	
	cran = "netgwas" 

	version("1.14.3", md5="921c10668fb347091bef5238489dae07")
	version("1.14.2", md5="fa827ef7c884be930d9595887134cea1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
