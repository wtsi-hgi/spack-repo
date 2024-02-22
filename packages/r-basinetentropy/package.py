# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasinetentropy(RPackage):
	"""Classification of RNA Sequences using Complex Network and
Information Theory

	It makes the creation of networks from sequences of RNA, with this is done the abstraction of characteristics of these networks with a methodology of maximum entropy for the purpose of making a classification between the classes of the sequences. There are two data present in the 'BASiNET' package, "mRNA", and "ncRNA" with 10 sequences. These sequences were taken from the data set used in the article (LI, Aimin; ZHANG, Junying; ZHOU, Zhongyin, 2014) <doi:10.1186/1471-2105-15-311>, these sequences are used to run examples. 
	"""
	
	cran = "BASiNETEntropy" 

	version("0.99.6", md5="bf8266297d0c91fb4528361658235d58")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
