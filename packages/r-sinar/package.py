# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinar(RPackage):
	"""Conditional Least Squared (CLS) Method for the Model SINAR(1,1)

	Implementation of the Conditional Least Square (CLS) estimates and
    its covariance matrix for the first-order spatial integer-valued
    autoregressive model (SINAR(1,1)) proposed by Ghodsi (2012)
    <doi:10.1080/03610926.2011.560739>.
	"""
	
	cran = "sinar" 

	version("0.1.0", md5="355ca48f918bbe58259bb693e70c37c4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
