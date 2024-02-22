# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStepdownfdp(RPackage):
	"""A Step-Down Procedure to Control the False Discovery Proportion

	Provides a step-down procedure for controlling the False
  Discovery Proportion (FDP) in a competition-based setup, implementing 
  Dong et al. (2020) <arXiv:2011.11939>. Such setups include target-decoy 
  competition (TDC) in computational mass spectrometry and the knockoff 
  construction in linear regression.
	"""
	
	homepage = "https://github.com/uni-Arya/stepdownfdp"
	cran = "stepdownfdp" 

	version("1.0.0", md5="808437620c6dca4324af48b618c53208")

	depends_on("r-pracma", type=("build", "run"))
