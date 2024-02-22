# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFaraway(RPackage):
	"""Functions and Datasets for Books by Julian Faraway

	Books are "Linear Models with R" published 1st Ed. August 2004, 2nd Ed. July 2014 by CRC press, ISBN 9781439887332, and "Extending the Linear Model with R" published by CRC press in 1st Ed. December 2005 and 2nd Ed. March 2016, ISBN 9781584884248 and "Practical Regression and ANOVA in R" contributed documentation on CRAN (now very dated).
	"""
	
	homepage = "https://github.com/julianfaraway/faraway"
	cran = "faraway" 

	version("1.0.8", md5="526488c5aa96fc1b152b922f28053feb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
