# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpcp(RPackage):
	"""Beta Product Confidence Procedure for Right Censored Data

	Calculates nonparametric pointwise confidence intervals for the survival distribution for right censored data, and for medians [Fay and Brittain <DOI:10.1002/sim.6905>]. Has two-sample tests for dissimilarity (e.g., difference, ratio or odds ratio) in survival at a fixed time, and differences in medians [Fay, Proschan, and Brittain <DOI:10.1111/biom.12231>]. Basically, the package gives exact inference methods for one- and two-sample exact inferences for Kaplan-Meier curves (e.g., generalizing Fisher's exact test to allow for right censoring), which are especially important for latter parts of the survival curve, small sample sizes or heavily censored data. Includes mid-p options.
	"""
	
	cran = "bpcp" 

	version("1.4.2", md5="2282c5640f31412bd31ff0c8830dc9ba")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
