# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasinet(RPackage):
	"""Classification of RNA Sequences using Complex Network Theory

	It makes the creation of networks from sequences of RNA, with this is done the abstraction of characteristics of these networks with a methodology of threshold for the purpose of making a classification between the classes of the sequences. There are four data present in the 'BASiNET' package, "sequences", "sequences2", "sequences-predict" and "sequences2-predict" with 11, 10, 11 and 11 sequences respectively. These sequences were taken from the data set used in the article (LI, Aimin; ZHANG, Junying; ZHOU, Zhongyin, 2014) <doi:10.1186/1471-2105-15-311>, these sequences are used to run examples. The BASiNET was published on Nucleic Acids Research, (ITO, Eric; KATAHIRA, Isaque; VICENTE, Fábio; PEREIRA, Felipe; LOPES, Fabrício, 2018) <doi:10.1093/nar/gky462>.
	"""
	
	cran = "BASiNET" 

	version("0.0.5", md5="54eb2d0303222b77f71c7dfa74c2b2ea")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rmcfs", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
