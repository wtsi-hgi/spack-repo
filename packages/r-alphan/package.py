# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphan(RPackage):
	"""Set Alpha Based on Sample Size Using Bayes Factors

	Sets the alpha level for coefficients in a regression model
    as a decreasing function of the sample size through the use of
    Jeffreys' Approximate Bayes factor. You tell alphaN() your sample
    size, and it tells you to which value you must lower alpha to avoid
    Lindley's Paradox. For details, see Wulff and Taylor (2023)
    <doi:10.31234/osf.io/3cbh7>.
	"""
	
	homepage = "https://github.com/jespernwulff/alphaN"
	cran = "alphaN" 

	version("0.1.0", md5="8b5b77116b9032709393d32a071664cd")

