# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesgof(RPackage):
	"""Bayesian Modeling via Frequentist Goodness-of-Fit

	A Bayesian data modeling scheme that performs four interconnected tasks: (i) characterizes the uncertainty of the elicited parametric prior; (ii) provides exploratory diagnostic for checking prior-data conflict; (iii) computes the final statistical prior density estimate; and (iv) executes macro- and micro-inference. Primary reference is Mukhopadhyay, S. and Fletcher, D. 2018 paper "Generalized Empirical Bayes via Frequentist Goodness of Fit" (<https://www.nature.com/articles/s41598-018-28130-5 >). 
	"""
	
	cran = "BayesGOF" 

	version("5.2", md5="3e674a8361330398607d1d3b10e5095e")

	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-bolstad2", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
