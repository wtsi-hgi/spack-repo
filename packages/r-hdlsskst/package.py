# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdlsskst(RPackage):
	"""Distribution-Free Exact High Dimensional Low Sample Size
k-Sample Tests

	Testing homogeneity of k multivariate distributions is a classical and challenging problem in
             statistics, and this becomes even more challenging when the dimension of the data exceeds the sample size.
             We construct some tests for this purpose which are exact level (size) alpha tests based on clustering. 
             These tests are easy to implement and distribution-free in finite sample situations. Under appropriate 
             regularity conditions, these tests have the consistency property in HDLSS asymptotic regime, where the 
             dimension of data grows to infinity while the sample size remains fixed. We also consider a multiscale 
             approach, where the results for different number of partitions are aggregated judiciously. Details are in 
             Biplab Paul, Shyamal K De and Anil K Ghosh (2021) <doi:10.1016/j.jmva.2021.104897>; Soham Sarkar and Anil K Ghosh (2019) 
             <doi:10.1109/TPAMI.2019.2912599>; William M Rand (1971) <doi:10.1080/01621459.1971.10482356>;  
             Cyrus R Mehta and Nitin R Patel (1983) <doi:10.2307/2288652>; Joseph C Dunn (1973) 
             <doi:10.1080/01969727308546046>; Sture Holm (1979) <doi:10.2307/4615733>; 
             Yoav Benjamini and Yosef Hochberg (1995) <doi: 10.2307/2346101>.
	"""
	
	cran = "HDLSSkST" 

	version("2.1.0", md5="adf550554df89f0db75ddab6e4e9cd99")

	depends_on("r-rcpp", type=("build", "run"))
