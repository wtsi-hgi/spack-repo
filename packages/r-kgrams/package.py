# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKgrams(RPackage):
	"""Classical k-gram Language Models

	
        Training and evaluating k-gram language models in R, 
        supporting several probability smoothing techniques, 
        perplexity computations, random text generation and more.
	"""
	
	homepage = "https://vgherard.github.io/kgrams/"
	cran = "kgrams" 

	version("0.2.0", md5="1d68b6c54b7025c21d492a12c882b156")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
