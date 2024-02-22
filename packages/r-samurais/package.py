# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamurais(RPackage):
	"""Statistical Models for the Unsupervised Segmentation of
Time-Series ('SaMUraiS')

	Provides a variety of original and flexible user-friendly 
    statistical latent variable models and unsupervised learning algorithms to 
    segment and represent time-series data (univariate or multivariate), and 
    more generally, longitudinal data, which include regime changes. 
    'samurais' is built upon the following packages, each of them is an 
    autonomous time-series segmentation approach: Regression with Hidden 
    Logistic Process ('RHLP'), Hidden Markov Model Regression ('HMMR'), 
    Multivariate 'RHLP' ('MRHLP'), Multivariate 'HMMR' ('MHMMR'), Piece-Wise 
    regression ('PWR'). For the advantages/differences of each of them, the 
    user is referred to our mentioned paper references.
	"""
	
	homepage = "https://github.com/fchamroukhi/SaMUraiS"
	cran = "samurais" 

	version("0.1.0", md5="7e51a79f41bada6f78311973cdef1f0c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
