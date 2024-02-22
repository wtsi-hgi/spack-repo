# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCubfits(RPackage):
	"""Codon Usage Bias Fits

	Estimating mutation and selection coefficients on synonymous
       codon bias usage based on models of ribosome overhead cost (ROC).
       Multinomial logistic regression and Markov Chain Monte Carlo are used to
       estimate and predict protein production rates with/without the presence
       of expressions and measurement errors. Work flows with examples for
       simulation, estimation and prediction processes are also provided
       with parallelization speedup. The whole framework is tested with
       yeast genome and gene expression data of Yassour, et al. (2009)
       <doi:10.1073/pnas.0812841106>.
	"""
	
	homepage = "https://github.com/snoweye/cubfits"
	cran = "cubfits" 

	version("0.1-4", md5="82c036a85cdab46c0ef60047c40e5a2d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
