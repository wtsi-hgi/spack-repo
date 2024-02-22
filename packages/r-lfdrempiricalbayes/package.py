# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfdrempiricalbayes(RPackage):
	"""Estimating Local False Discovery Rates Using Empirical Bayes
Methods

	New empirical Bayes methods aiming at analyzing the association of single nucleotide polymorphisms (SNPs) to some particular disease are implemented in this package. The package uses local false discovery rate (LFDR) estimates of SNPs within a sample population defined as a  "reference class" and discovers if SNPs are associated with the corresponding disease. Although SNPs are used throughout this document, other biological data such as protein data and other gene data can be used. Karimnezhad, Ali and Bickel, D. R. (2016) <http://hdl.handle.net/10393/34889>.
	"""
	
	homepage = "https://davidbickel.com"
	cran = "LFDREmpiricalBayes" 

	version("1.0", md5="5df702e37dc227be1d10c34ef4dfb4f8")

	depends_on("r@2.14.2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
