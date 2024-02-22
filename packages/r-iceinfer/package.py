# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIceinfer(RPackage):
	"""Incremental Cost-Effectiveness Inference using Two Unbiased
Samples

	Given two unbiased samples of patient level data on cost and effectiveness
  for a pair of treatments, make head-to-head treatment comparisons by (i) generating the
  bivariate bootstrap resampling distribution of ICE uncertainty for a specified value of
  the shadow price of health, lambda, (ii) form the wedge-shaped ICE confidence region with
  specified confidence fraction within [0.50, 0.99] that is equivariant with respect to
  changes in lambda, (iii) color the bootstrap outcomes within the above confidence wedge
  with economic preferences from an ICE map with specified values of lambda, beta and gamma
  parameters, (iv) display VAGR and ALICE acceptability curves, and (v) illustrate variation
  in ICE preferences by displaying potentially non-linear indifference(iso-preference) curves
  from an ICE map with specified values of lambda, beta and either gamma or eta parameters. 
	"""
	
	homepage = "https://www.R-project.org"
	cran = "ICEinfer" 

	version("1.3", md5="88d0b4fff7bf1e94b0b73e8ba381e7cf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
