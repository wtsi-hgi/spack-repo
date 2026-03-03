# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvyweight(RPackage):
	"""Quick and Flexible Survey Weighting

	Quickly and flexibly calculates weights for survey data, in order to correct
    for survey non-response or other sampling issues. Uses rake weighting, a common technique 
    also know as rim weighting or iterative proportional fitting.  This technique allows for weighting 
    on multiple variables, even when the interlocked distribution of the two
    variables is not known. Interacts with Thomas Lumley's 'survey' package, as described in 
    Lumley, Thomas (2011, ISBN:978-1-118-21093-2). Adds additional functionality, more adaptable syntax, and error-checking
    to the base weighting functionality in 'survey.'
	"""
	
	cran = "svyweight" 

	version("0.1.0", md5="f5e1bb3371c01510e5ed9066cfb45fcc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
