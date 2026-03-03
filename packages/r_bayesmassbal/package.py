# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmassbal(RPackage):
	"""Bayesian Data Reconciliation of Separation Processes

	Bayesian tools that can be used to reconcile, or mass balance, mass flow rate data collected from chemical or particulate separation processes aided by constraints governed by the conservation of mass.
    Functions included in the package aid the user in organizing and constraining data, using Markov chain Monte Carlo methods to obtain samples from Bayesian models, and in computation of the marginal likelihood of the data, given a particular model, for model selection.  Marginal likelihood is approximated by methods in Chib S (1995) <doi:10.2307/2291521>.
	"""
	
	homepage = "https://github.com/skoermer/BayesMassBal"
	cran = "BayesMassBal" 

	version("1.1.0", md5="8ca540ca99f02ce386cc01b99fdccbc5")

	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-laplacesdemon", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
