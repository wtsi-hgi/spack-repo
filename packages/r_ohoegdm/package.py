# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROhoegdm(RPackage):
	"""Ordinal Higher-Order Exploratory General Diagnostic Model for
Polytomous Data

	Perform a Bayesian estimation of the ordinal exploratory 
    Higher-order General Diagnostic Model (OHOEGDM) for Polytomous Data 
    described by Culpepper, S. A. and Balamuta, J. J. (In Press) <doi:10.1080/00273171.2021.1985949>.
	"""
	
	homepage = "https://github.com/tmsalab/ohoegdm"
	cran = "ohoegdm" 

	version("0.1.0", md5="2cfccf962c7d4f22a370805edcbec772")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
