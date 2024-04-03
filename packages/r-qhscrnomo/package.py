# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQhscrnomo(RPackage):
	"""Construct Nomograms for Competing Risks Regression Models

	Nomograms are constructed to predict the cumulative incidence
    rate which is calculated after adjusting for competing causes to the event of interest. 
    K-fold cross-validation is implemented to validate predictive accuracy using a competing-risk version of the concordance index.
    Methods are as described in: Kattan MW, Heller G, 
    Brennan MF (2003).
	"""
	
	homepage = "https://github.com/ClevelandClinicQHS/QHScrnomo"
	cran = "QHScrnomo" 

	version("3.0.1", md5="51167b4274a008700ac73a5d98f2b290")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
