# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynthetic(RPackage):
	"""Synthetic Experience Tracking Insurance Claims

	Creation of an individual claims simulator which generates various
    features of non-life insurance claims. An initial set of test parameters,
    designed to mirror the experience of an Auto Liability portfolio, were set
    up and applied by default to generate a realistic test data set of
    individual claims (see vignette). The simulated data set then allows
    practitioners to back-test the validity of various reserving models and to
    prove and/or disprove certain actuarial assumptions made in claims
    modelling. The distributional assumptions used to generate this data set can
    be easily modified by users to match their experiences. Reference: Avanzi B,
    Taylor G, Wang M, Wong B (2020) "SynthETIC: an individual insurance claim
    simulator with feature control" <arXiv:2008.05693>.
	"""
	
	homepage = "https://github.com/agi-lab/SynthETIC"
	cran = "SynthETIC" 

	version("1.1.0", md5="a57c4f459c4fdd10e90db2cdea9d08cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
