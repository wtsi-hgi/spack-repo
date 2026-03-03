# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzgp(RPackage):
	"""Easy-to-Interpret Gaussian Process Models for Computer
Experiments

	Fit model for datasets with easy-to-interpret Gaussian process modeling, predict responses for new inputs.
    The input variables of the datasets can be quantitative, qualitative/categorical or mixed.
    The output variable of the datasets is a scalar (quantitative).
    The optimization of the likelihood function can be chosen by the users (see the documentation of EzGP_fit()).
    The modeling method is published in "EzGP: Easy-to-Interpret Gaussian Process Models for Computer Experiments with Both Quantitative and Qualitative Factors" 
    by Qian Xiao, Abhyuday Mandal, C. Devon Lin, and Xinwei Deng (2022) <doi:10.1137/19M1288462>. 
	"""
	
	cran = "EzGP" 

	version("0.1.0", md5="ff7a0d1d82376773a2c741cd708a23a0")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-nloptr@2.0.3:", type=("build", "run"))
