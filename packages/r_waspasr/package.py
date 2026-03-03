# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaspasr(RPackage):
	"""Tool Kit to Implement a W.A.S.P.A.S. Based Multi-Criteria
Decision Analysis Solution

	Provides a set of functions to implement decision-making systems
    based on the W.A.S.P.A.S. method (Weighted Aggregated Sum Product Assessment),
    Chakraborty and Zavadskas (2012) <doi:10.5755/j01.eee.122.6.1810>.
    So this package offers functions that analyze and validate the
    raw data, which must be entered in a determined format;
    extract specific vectors and matrices from this raw database;
    normalize the input data; calculate rankings by intermediate methods;
    apply the lambda parameter for the main method; and a function that does
    everything at once. The package has an example database called choppers,
    with which the user can see how the input data should be organized so that
    everything works as recommended by the decision methods based on multiple
    criteria that this package solves. Basically, the data are composed of a set
    of alternatives, which will be ranked, a set of choice criteria, a matrix
    of values for each Alternative-Criterion relationship, a vector of weights
    associated with the criteria, since certain criteria are considered more
    important than others, as well as a vector that defines each criterion as
    cost or benefit, this determines the calculation formula, as there are those
    criteria that we want the highest possible value (e.g. durability)
    and others that we want the lowest possible value (e.g. price).
	"""
	
	cran = "waspasR" 

	version("0.1.5", md5="3d7129c0dbc0a16ec8fb647e1e6236c4")

	depends_on("r@4.2:", type=("build", "run"))
