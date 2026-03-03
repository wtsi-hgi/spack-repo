# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaggr(RPackage):
	"""Supporting Files and Functions for the Book Bayesian Modelling
with 'JAGS'

	All the data and functions used to produce the book. We do not expect
    most people to use the package for any other reason than to get simple access to the
    'JAGS' model files, the data, and perhaps run some of the simple examples.
    The authors of the book are David Lucy (now sadly deceased) and James Curran. It is 
    anticipated that a manuscript will be provided to Taylor and Francis around February 2020, with
    bibliographic details to follow at that point. Until such time, further information
    can be obtained by emailing James Curran.
	"""
	
	cran = "jaggR" 

	version("0.1.1", md5="54e35373e608baf57c3bdbcdbda75ba7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
