# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtgt(RPackage):
	"""Closed Testing with Globaltest for Pathway Analysis

	A shortcut procedure is proposed to implement closed testing for large-scale multiple testings, especially with the global test. This shortcut is asymptotically equivalent to closed testing and post hoc. Users could detect any possible sets of features or pathways with family-wise error rate controlled. The global test is powerful to detect associations between a group of features and an outcome of interest. 
	"""
	
	cran = "ctgt" 

	version("2.0.1", md5="c1310821952207e03df36c8f356cca27")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
