# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAster(RPackage):
	"""Aster Models

	Aster models (Geyer, Wagenius, and Shaw, 2007,
    <doi:10.1093/biomet/asm030>; Shaw, Geyer, Wagenius, Hangelbroek, and
    Etterson, 2008, <doi:10.1086/588063>; Geyer, Ridley, Latta, Etterson,
    and Shaw, 2013, <doi:10.1214/13-AOAS653>) are exponential family
    regression models for life
    history analysis.  They are like generalized linear models except that
    elements of the response vector can have different families (e. g.,
    some Bernoulli, some Poisson, some zero-truncated Poisson, some normal)
    and can be dependent, the dependence indicated by a graphical structure.
    Discrete time survival analysis, life table analysis,
    zero-inflated Poisson regression, and
    generalized linear models that are exponential family (e. g., logistic
    regression and Poisson regression with log link) are special cases.
    Main use is for data in which there is survival over discrete time periods
    and there is additional data about what happens conditional on survival
    (e. g., number of offspring).  Uses the exponential family canonical
    parameterization (aster transform of usual parameterization).
    There are also random effects versions of these models.
	"""
	
	homepage = "http://www.stat.umn.edu/geyer/aster/"
	cran = "aster" 

	version("1.1-3", md5="ef30659f6bb9f210644bab14bbe4a6bf")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
