# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQra(RPackage):
	"""Quantal Response Analysis for Dose-Mortality Data

	Functions are provided that implement the 
    use of the Fieller's formula methodology, for 
    calculating a confidence interval for a ratio of
    (commonly, correlated) means.  See Fieller (1954)
    <doi:10.1111/j.2517-6161.1954.tb00159.x>.  Here,
    the application of primary interest is to studies
    of insect mortality response to increasing doses
    of a fumigant, or, e.g., to time in coolstorage.
    The formula is used to calculate a confidence
    interval for the dose or time required to achieve
    a specified mortality proportion, commonly 0.5 
    or 0.99.  Vignettes demonstrate link functions
    that may be considered, checks on fitted models,
    and alternative choices of error family.  Note
    in particular the betabinomial error family.
    See also Maindonald, Waddell, and Petry (2001) 
    <doi:10.1016/S0925-5214(01)00082-5>.
	"""
	
	homepage = "https://github.com/jhmaindonald/qra"
	cran = "qra" 

	version("0.2.7", md5="1e5f02c5e32ee81cae33a9701106e163")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
