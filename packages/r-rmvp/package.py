# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmvp(RPackage):
	"""Memory-Efficient, Visualize-Enhanced, Parallel-Accelerated GWAS
Tool

	A memory-efficient, visualize-enhanced, parallel-accelerated Genome-Wide Association Study (GWAS) tool. It can
    (1) effectively process large data, 
    (2) rapidly evaluate population structure, 
    (3) efficiently estimate variance components several algorithms, 
    (4) implement parallel-accelerated association tests of markers three methods, 
    (5) globally efficient design on GWAS process computing, 
    (6) enhance visualization of related information. 
    'rMVP' contains three models GLM (Alkes Price (2006) <DOI:10.1038/ng1847>), MLM (Jianming Yu (2006) <DOI:10.1038/ng1702>) 
    and FarmCPU (Xiaolei Liu (2016) <doi:10.1371/journal.pgen.1005767>); variance components estimation methods EMMAX 
    (Hyunmin Kang (2008) <DOI:10.1534/genetics.107.080101>;), FaSTLMM (method: Christoph Lippert (2011) <DOI:10.1038/nmeth.1681>, 
    R implementation from 'GAPIT2': You Tang and Xiaolei Liu (2016) <DOI:10.1371/journal.pone.0107684> and 
    'SUPER': Qishan Wang and Feng Tian (2014) <DOI:10.1371/journal.pone.0107684>), and HE regression 
    (Xiang Zhou (2017) <DOI:10.1214/17-AOAS1052>).
	"""
	
	homepage = "https://github.com/xiaolei-lab/rMVP"
	cran = "rMVP" 

	version("1.0.8", md5="28808b787a1b25be94551324d2c6c4c6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
