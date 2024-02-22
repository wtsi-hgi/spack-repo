# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhor(RPackage):
	"""Rho for Inter Rater Reliability

	Rho is used to test the generalization of inter rater reliability
    (IRR) statistics. Calculating rho starts by generating a large number of
    simulated, fully-coded data sets: a sizable collection of hypothetical
    populations, all of which have a kappa value below a given threshold -- which
    indicates unacceptable agreement. Then kappa is calculated on a sample from
    each of those sets in the collection to see if it is equal to or higher than
    the kappa in then real sample. If less than five percent of the distribution
    of samples from the simulated data sets is greater than actual observed kappa,
    the null hypothesis is rejected and one can conclude that if the two raters had
    coded the rest of the data, we would have acceptable agreement (kappa above the
    threshold).
	"""
	
	homepage = "https://rhor.qe-libs.org"
	cran = "rhoR" 

	version("1.3.0.3", md5="2eb2309215bffd5dace0676d6eda7548")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
