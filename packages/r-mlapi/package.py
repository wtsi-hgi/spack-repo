# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlapi(RPackage):
	"""Abstract Classes for Building 'scikit-learn' Like API

	Provides 'R6' abstract classes for building machine learning models 
    with 'scikit-learn' like API. <https://scikit-learn.org/> is a popular module 
    for 'Python' programming language which design became de facto a standard 
    in industry for machine learning tasks.
	"""
	
	cran = "mlapi" 

	version("0.1.1", md5="7003dc9966bf251bc9f35dfc501ee74d")

	depends_on("r-r6@2.2.1:", type=("build", "run"))
	depends_on("r-matrix@1.1:", type=("build", "run"))
