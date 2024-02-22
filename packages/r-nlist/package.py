# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlist(RPackage):
	"""Lists of Numeric Atomic Objects

	Create and manipulate numeric list ('nlist') objects.  An
    'nlist' is an S3 list of uniquely named numeric objects.  An numeric
    object is an integer or double vector, matrix or array.  An 'nlists'
    object is a S3 class list of 'nlist' objects with the same names,
    dimensionalities and typeofs.  Numeric list objects are of interest
    because they are the raw data inputs for analytic engines such as
    'JAGS', 'STAN' and 'TMB'.  Numeric lists objects, which are useful for
    storing multiple realizations of of simulated data sets, can be
    converted to coda::mcmc and coda::mcmc.list objects.
	"""
	
	homepage = "https://github.com/poissonconsulting/nlist"
	cran = "nlist" 

	version("0.3.3", md5="9c2d6878a422f748aba755de81505150")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-extras", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-term", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-universals", type=("build", "run"))
