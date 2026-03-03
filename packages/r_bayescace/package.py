# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayescace(RPackage):
	"""Bayesian Model for CACE Analysis

	Performs CACE (Complier Average Causal Effect analysis) on either a single study or meta-analysis of datasets with binary outcomes, using either complete or incomplete noncompliance information. Our package implements the Bayesian methods proposed in Zhou et al. (2019) <doi:10.1111/biom.13028>, which introduces a Bayesian hierarchical model for estimating CACE in meta-analysis of clinical trials with noncompliance, and Zhou et al. (2021) <doi:10.1080/01621459.2021.1900859>, with an application example on Epidural Analgesia.
	"""
	
	cran = "BayesCACE" 

	version("1.2.3", md5="2b50eeb63cf9c3f4a4e4dce4b2f7604a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjags@4.6:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("jags@4.0.0:4.999.999", type=("build", "link", "run"))
