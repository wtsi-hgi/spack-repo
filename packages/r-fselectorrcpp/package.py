# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFselectorrcpp(RPackage):
	"""'Rcpp' Implementation of 'FSelector' Entropy-Based Feature
Selection Algorithms with a Sparse Matrix Support

	'Rcpp' (free of 'Java'/'Weka') implementation of 'FSelector' entropy-based feature selection 
 algorithms based on an MDL discretization (Fayyad U. M., Irani K. B.: Multi-Interval Discretization of Continuous-Valued Attributes for Classification Learning.
 In 13'th International Joint Conference on Uncertainly in Artificial Intelligence (IJCAI93), pages 1022-1029, Chambery, France, 1993.) <https://www.ijcai.org/Proceedings/93-2/Papers/022.pdf>
 with a sparse matrix support.
	"""
	
	homepage = "https://github.com/mi2-warsaw/FSelectorRcpp"
	cran = "FSelectorRcpp" 

	version("0.3.11", md5="c970052e14a17ee94b7b3e22340846f9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
