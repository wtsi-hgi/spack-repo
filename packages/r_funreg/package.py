# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunreg(RPackage):
	"""Functional Regression for Irregularly Timed Data

	Performs functional regression, and some related
    approaches, for intensive longitudinal data (see the book by Walls & Schafer, 
    2006, Models for Intensive Longitudinal Data, Oxford) when such data is not
    necessarily observed on an equally spaced grid of times.  The
    approach generally follows the ideas of Goldsmith, Bobb, Crainiceanu,
    Caffo, and Reich (2011)<DOI:10.1198/jcgs.2010.10007> and the approach taken in their sample code, but
    with some modifications to make it more feasible to use with long rather
    than wide, non-rectangular longitudinal datasets with unequal and
    potentially random measurement times.  It also allows easy plotting of the
    correlation between the smoothed covariate and the outcome as a function of
    time, which can add additional insights on how to interpret a functional
    regression.  Additionally, it also provides several permutation tests for
    the significance of the functional predictor.  The heuristic interpretation
    of ``time'' is used to describe the index of the functional predictor, but
    the same methods can equally be used for another unidimensional continuous
    index, such as space along a north-south axis.  Note that most of the functionality
	of this package has been superseded by added features after 2016 in the 'pfr' function by
    Jonathan Gellar, Mathew W. McLean, Jeff Goldsmith, and Fabian Scheipl, in the 
	'refund' package built by Jeff Goldsmith and co-authors and maintained by Julia Wrobel.
	The development of the funreg package in 2015 and 2016 was part of a research 
	project supported by Award R03 CA171809-01 from the National Cancer Institute and Award P50 
	DA010075 from the National Institute on Drug Abuse. The content is solely the responsibility of the
    authors and does not necessarily represent the official views of the
    National Institute on Drug Abuse, the National Cancer Institute, or the
    National Institutes of Health.
	"""
	
	cran = "funreg" 

	version("1.2.2", md5="ac9f527f3e71d2dfb76dc648f713b9b5")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
