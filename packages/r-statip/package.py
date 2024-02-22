# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatip(RPackage):
	"""Statistical Functions for Probability Distributions and
Regression

	A collection of miscellaneous statistical functions for 
    probability distributions: 'dbern()', 'pbern()', 'qbern()', 'rbern()' for 
    the Bernoulli distribution, and 'distr2name()', 'name2distr()' for 
    distribution names; 
    probability density estimation: 'densityfun()'; 
    most frequent value estimation: 'mfv()', 'mfv1()'; 
    other statistical measures of location: 'cv()' (coefficient of variation),
    'midhinge()', 'midrange()', 'trimean()'; 
    construction of histograms: 'histo()', 'find_breaks()'; 
    calculation of the Hellinger distance: 'hellinger()'; 
    use of classical kernels: 'kernelfun()', 'kernel_properties()'; 
    univariate piecewise-constant regression: 'picor()'. 
	"""
	
	homepage = "https://github.com/paulponcet/statip"
	cran = "statip" 

	version("0.2.3", md5="afa8bc4b690cf4a275a785800dda055a")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
