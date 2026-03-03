# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimark(RPackage):
	"""Capture-Mark-Recapture Analysis using Multiple Non-Invasive
Marks

	Traditional and spatial capture-mark-recapture analysis with
    multiple non-invasive marks. The models implemented in 'multimark' combine
    encounter history data arising from two different non-invasive "marks",
    such as images of left-sided and right-sided pelage patterns of bilaterally
    asymmetrical species, to estimate abundance and related demographic
    parameters while accounting for imperfect detection. Bayesian models are
    specified using simple formulae and fitted using Markov chain Monte Carlo.
    Addressing deficiencies in currently available software, 'multimark' also
    provides a user-friendly interface for performing Bayesian multimodel
    inference using non-spatial or spatial capture-recapture data consisting of a single
    conventional mark or multiple non-invasive marks. See McClintock (2015) <doi:10.1002/ece3.1676> and Maronde et al. (2020) <doi:10.1002/ece3.6990>.
	"""
	
	cran = "multimark" 

	version("2.1.6", md5="2e04118f473fd08dabe77765e8f0adf1")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rmark", type=("build", "run"))
	depends_on("r-brobdingnag", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
