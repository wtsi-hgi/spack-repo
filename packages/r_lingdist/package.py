# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLingdist(RPackage):
	"""Fast Linguistic Distance and Alignment Computation

	A fast generalized edit distance and string alignment computation mainly for linguistic aims. As a generalization to the classic edit distance algorithms, the package allows users to define custom cost for every symbol's insertion, deletion, and substitution. The package also allows character combinations in any length to be seen as a single symbol which is very useful for International Phonetic Alphabet (IPA) transcriptions with diacritics. In addition to edit distance result, users can get detailed alignment information such as all possible alignment scenarios between two strings which is useful for testing, illustration or any further usage. Either the distance matrix or its long table form can be obtained and tools to do such conversions are provided. All functions in the package are implemented in 'C++' and the distance matrix computation is parallelized leveraging the 'RcppThread' package.
	"""
	
	homepage = "https://github.com/fncokg/lingdist"
	cran = "lingdist" 

	version("1.0", md5="787fc9ee75026e5e9d34b1e59f421ff7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
