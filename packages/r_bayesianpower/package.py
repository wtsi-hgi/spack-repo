# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesianpower(RPackage):
	"""Sample Size and Power for Comparing Inequality Constrained
Hypotheses

	A collection of methods to determine the required sample size for
    the evaluation of inequality constrained hypotheses by means of a Bayes 
    factor. Alternatively, for a given sample size, the unconditional error 
    probabilities or the expected conditional error probabilities can be
    determined. Additional material on the methods in this package is 
    available in Klaassen, F., Hoijtink, H. & Gu, X. (2019) 
    <doi:10.31219/osf.io/d5kf3>.
	"""
	
	cran = "BayesianPower" 

	version("0.2.3", md5="25d056cfe62158ca355da9cfd3c6b5b8")

