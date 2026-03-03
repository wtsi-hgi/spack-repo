# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeaturehashing(RPackage):
	"""Creates a Model Matrix via Feature Hashing with a Formula
Interface

	Feature hashing, also called as the hashing trick, is a method to transform 
  features of a instance to a vector. Thus, it is a method to transform a real dataset to a matrix. 
  Without looking up the indices in an associative array, 
  it applies a hash function to the features and uses their hash values as indices directly.
  The method of feature hashing in this package was proposed in Weinberger et al. (2009) <arXiv:0902.2206>. 
  The hashing algorithm is the murmurhash3 from the 'digest' package. 
  Please see the README in <https://github.com/wush978/FeatureHashing> for more information.
	"""
	
	homepage = "https://github.com/wush978/FeatureHashing"
	cran = "FeatureHashing" 

	version("0.9.2", md5="50f32b1a61ed781d8e1a90071dca0230")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-digest@0.6.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-bh@1.54.0.1:", type=("build", "run"))
