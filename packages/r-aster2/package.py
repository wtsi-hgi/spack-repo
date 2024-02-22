# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAster2(RPackage):
	"""Aster Models

	Aster models are exponential family regression models for life
    history analysis.  They are like generalized linear models except that
    elements of the response vector can have different families (e. g.,
    some Bernoulli, some Poisson, some zero-truncated Poisson, some normal)
    and can be dependent, the dependence indicated by a graphical structure.
    Discrete time survival analysis, zero-inflated Poisson regression, and
    generalized linear models that are exponential family (e. g., logistic
    regression and Poisson regression with log link) are special cases.
    Main use is for data in which there is survival over discrete time periods
    and there is additional data about what happens conditional on survival
    (e. g., number of offspring).  Uses the exponential family canonical
    parameterization (aster transform of usual parameterization).
    Unlike the aster package, this package does dependence groups (nodes of
    the graph need not be conditionally independent given their predecessor
    node), including multinomial and two-parameter normal as families.  Thus
    this package also generalizes mark-capture-recapture analysis.
	"""
	
	homepage = "http://www.stat.umn.edu/geyer/aster/"
	cran = "aster2" 

	version("0.3", md5="90524dd93d05055365ea64ad0e2710d1", url="https://cran.r-project.org/src/contrib/aster2_0.3.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
