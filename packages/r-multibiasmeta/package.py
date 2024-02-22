# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibiasmeta(RPackage):
	"""Sensitivity Analysis for Multiple Biases in Meta-Analyses

	Meta-analyses can be compromised by studies' internal biases (e.g.,
  confounding in nonrandomized studies) as well as by publication bias. This
  package conducts sensitivity analyses for the joint effects of these biases
  (per Mathur (2022) <doi:10.31219/osf.io/u7vcb>). These sensitivity analyses 
  address two questions: (1) For a given severity of internal bias across
  studies and of publication bias, how much could the results change?; and
  (2) For a given severity of publication bias, how severe would internal bias
  have to be, hypothetically, to attenuate the results to the null or by a given
  amount?
	"""
	
	homepage = "https://github.com/mathurlabstanford/multibiasmeta"
	cran = "multibiasmeta" 

	version("0.2.2", md5="a11387df0867380fa4f02675bb408421")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-evalue", type=("build", "run"))
	depends_on("r-metabias", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-robumeta", type=("build", "run"))
