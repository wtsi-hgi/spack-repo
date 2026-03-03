# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRr(RPackage):
	"""Statistical Methods for the Randomized Response Technique

	Enables researchers to conduct multivariate statistical analyses
    of survey data with randomized response technique items from several designs,
    including mirrored question, forced question, and unrelated question. This
    includes regression with the randomized response as the outcome and logistic
    regression with the randomized response item as a predictor. In addition,
    tools for conducting power analysis for designing randomized response items
    are included. The package implements methods described in Blair, Imai, and Zhou
    (2015) ''Design and Analysis of the Randomized Response Technique,'' Journal
    of the American Statistical Association 
    <https://graemeblair.com/papers/randresp.pdf>.
	"""
	
	cran = "rr" 

	version("1.4.2", md5="2687de760e424b96d94b1b5047832de1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
