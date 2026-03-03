# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAldvmm(RPackage):
	"""Adjusted Limited Dependent Variable Mixture Models

	The goal of the package 'aldvmm' is to fit adjusted limited 
    dependent variable mixture models of health state utilities. Adjusted 
    limited dependent variable mixture models are finite mixtures of normal 
    distributions with an accumulation of density mass at the limits, and a gap 
    between 100% quality of life and the next smaller utility value. The 
    package 'aldvmm' uses the likelihood and expected value functions proposed 
    by Hernandez Alava and Wailoo (2015) <doi:10.1177/1536867X1501500307> using 
    normal component distributions and a multinomial logit model of 
    probabilities of component membership.
	"""
	
	homepage = "https://github.com/pletschm/aldvmm/"
	cran = "aldvmm" 

	version("0.8.8", md5="c6f7cd4505333db7d9a34df02baa2034")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
