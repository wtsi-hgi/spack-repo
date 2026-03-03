# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastnaivebayes(RPackage):
	"""Extremely Fast Implementation of a Naive Bayes Classifier

	This is an extremely fast implementation of a Naive Bayes classifier. This 
    package is currently the only package that supports a Bernoulli distribution, a Multinomial 
    distribution, and a Gaussian distribution, making it suitable for both binary features, 
    frequency counts, and numerical features. Another feature is the support of a mix of 
    different event models. Only numerical variables are allowed, however, categorical variables 
    can be transformed into dummies and used with the Bernoulli distribution. 
    The implementation is largely based on the paper 
    "A comparison of event models for Naive Bayes anti-spam e-mail filtering" 
    written by K.M. Schneider (2003) <doi:10.3115/1067807.1067848>. Any issues can be 
    submitted to: <https://github.com/mskogholt/fastNaiveBayes/issues>.
	"""
	
	homepage = "https://github.com/mskogholt/fastNaiveBayes"
	cran = "fastNaiveBayes" 

	version("2.2.1", md5="2562fb099498bb20481defef5f5f37b1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
