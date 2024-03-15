# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFhmm(RPackage):
	"""Fitting Hidden Markov Models to Financial Data

	Fitting (hierarchical) hidden Markov models to financial data
    via maximum likelihood estimation. See Oelschläger, L. and Adam, T.
    "Detecting bearish and bullish markets in financial time series using 
    hierarchical hidden Markov models" (2021, Statistical Modelling) 
    <doi:10.1177/1471082X211034048> for a reference.
	"""
	
	homepage = "https://loelschlaeger.de/fHMM/"
	cran = "fHMM" 

	version("1.2.2", md5="5b46819cf413f5764b1b1f5998e4a9df")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-oeli@0.3:", type=("build", "run"))
	depends_on("r-padr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
