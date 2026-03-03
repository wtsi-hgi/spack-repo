# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvsem(RPackage):
	"""SEM Model Comparison with K-Fold Cross-Validation

	The goal of 'cvsem' is to provide functions that allow for comparing Structural Equation Models (SEM) using cross-validation. Users can specify multiple SEMs using 'lavaan' syntax. 'cvsem' computes the Kullback Leibler (KL) Divergence between 1) the model implied covariance matrix estimated from the training data and 2) the sample covariance matrix estimated from the test data described in Cudeck, Robert & Browne (1983) <doi:10.18637/jss.v048.i02>. The KL Divergence is computed for each of the specified SEMs allowing for the models to be compared based on their prediction errors. 
	"""
	
	cran = "cvsem" 

	version("1.0.0", md5="f67e5c731eca13ca81b8b8e6ef636bb2")

	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
