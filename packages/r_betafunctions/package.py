# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBetafunctions(RPackage):
	"""Functions for Working with Two- And Four-Parameter Beta
Probability Distributions and Psychometric Analysis of
Classifications

	Package providing a number of functions for working with Two- and 
    Four-parameter Beta and closely related distributions (i.e., the Gamma-
    Binomial-, and Beta-Binomial distributions).
        Includes, among other things: 
    - d/p/q/r functions for Four-Parameter Beta distributions and Generalized
    "Binomial" (continuous) distributions, and d/p/r- functions for Beta-
    Binomial distributions.
    - d/p/q/r functions for Two- and Four-Parameter Beta distributions
    parameterized in terms of their means and variances rather than their
    shape-parameters.
    - Moment generating functions for Binomial distributions, Beta-Binomial 
    distributions, and observed value distributions.
    - Functions for estimating classification accuracy and consistency, 
    making use of the Classical Test-Theory based 'Livingston and Lewis' (L&L) 
    and 'Hanson and Brennan' approaches.
      A shiny app is available, providing a GUI for the L&L approach when used 
    for binary classifications. For url to the app, see documentation for the 
    LL.CA() function.
    Livingston and Lewis (1995) <doi:10.1111/j.1745-3984.1995.tb00462.x>.
    Lord (1965) <doi:10.1007/BF02289490>.
    Hanson (1991) <https://files.eric.ed.gov/fulltext/ED344945.pdf>.
	"""
	
	cran = "betafunctions" 

	version("1.9.0", md5="5e9b7adea2ff11e937eba3d68630cd03")
	version("1.8.1", md5="05bf901a5303b342478190af741d20bd")

