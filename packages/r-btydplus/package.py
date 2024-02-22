# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBtydplus(RPackage):
	"""Probabilistic Models for Assessing and Predicting your Customer
Base

	Provides advanced statistical methods to describe and predict customers'
  purchase behavior in a non-contractual setting. It uses historic transaction records to fit a
  probabilistic model, which then allows to compute quantities of managerial interest on a cohort-
  as well as on a customer level (Customer Lifetime Value, Customer Equity, P(alive), etc.). This
  package complements the BTYD package by providing several additional buy-till-you-die models, that
  have been published in the marketing literature, but whose implementation are complex and non-trivial.
  These models are: NBD [Ehrenberg (1959) <doi:10.2307/2985810>], MBG/NBD [Batislam et al (2007) 
  <doi:10.1016/j.ijresmar.2006.12.005>], (M)BG/CNBD-k [Reutterer et al (2020) 
  <doi:10.1016/j.ijresmar.2020.09.002>], Pareto/NBD (HB) [Abe (2009) <doi:10.1287/mksc.1090.0502>] 
  and Pareto/GGG [Platzer and Reutterer (2016) <doi:10.1287/mksc.2015.0963>].
	"""
	
	homepage = "https://github.com/mplatzer/BTYDplus#readme"
	cran = "BTYDplus" 

	version("1.2.0", md5="a3cb47d9e9e1463ec55adab7065a553d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-btyd@2.3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-bayesm", type=("build", "run"))
