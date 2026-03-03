# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabularmlc(RPackage):
	"""Tabular Maximum Likelihood Classifier

	
  The maximum likelihood classifier (MLC) is one of the most common classifiers used for 
  remote sensing imagery. 
  This package uses 'RcppArmadillo' to provide a fast implementation of the MLC to train 
  and predict over tabular data (data.frame).
  The algorithms were based on Mather (1985) <doi:10.1080/01431168508948456> method.
	"""
	
	homepage = "https://github.com/caiohamamura/tabularMLC"
	cran = "tabularMLC" 

	version("0.0.3", md5="f2cd3ff00c5fd88b68da29e6a30b626c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
