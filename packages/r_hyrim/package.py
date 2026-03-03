# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyrim(RPackage):
	"""Multicriteria Risk Management using Zero-Sum Games with
Vector-Valued Payoffs that are Probability Distributions

	Construction and analysis of multivalued zero-sum matrix games over the abstract space of probability distributions, which describe the losses in each scenario of defense vs. attack action. The distributions can be compiled directly from expert opinions or other empirical data (insofar available). The package implements the methods put forth in the EU project HyRiM (Hybrid Risk Management for Utility Networks), FP7 EU Project Number 608090. The method has been published in Rass, S., König, S., Schauer, S., 2016. Decisions with Uncertain Consequences-A Total Ordering on Loss-Distributions. PLoS ONE 11, e0168583. <doi:10.1371/journal.pone.0168583>, and applied for advanced persistent thread modeling in Rass, S., König, S., Schauer, S., 2017. Defending Against Advanced Persistent Threats Using Game-Theory. PLoS ONE 12, e0168675. <doi:10.1371/journal.pone.0168675>. A volume covering the wider range of aspects of risk management, partially based on the theory implemented in the package is the book edited by S. Rass and S. Schauer, 2018. Game Theory for Security and Risk Management: From Theory to Practice. Springer, <doi:10.1007/978-3-319-75268-6>, ISBN 978-3-319-75267-9.
	"""
	
	cran = "HyRiM" 

	version("2.0.2", md5="c85aaa454adf07c30e4a86fc4ba7d48e")

	depends_on("r-compare", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
	depends_on("r-grimport2", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
