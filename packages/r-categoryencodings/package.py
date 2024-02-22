# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCategoryencodings(RPackage):
	"""Category Variable Encodings

	Simple, fast, and automatic encodings for category data using 
             a data.table backend. Most of the methods are an implementation 
             of "Sufficient Representation for Categorical Variables" by
             Johannemann, Hadad, Athey, Wager (2019) <arXiv:1908.09874>,
             particularly their mean, sparse principal component analysis, 
             low rank representation, and multinomial logit encodings.
	"""
	
	homepage = "https://github.com/JSzitas/categoryEncodings"
	cran = "categoryEncodings" 

	version("1.4.3", md5="002564d7ad257efbaff941dc19326079")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-sparsepca", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
