# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDenoiseq(RPackage):
	"""Differential Expression Analysis Using a Bottom-Up Model

	Given count data from two conditions, it determines which transcripts are differentially expressed across the two conditions using Bayesian inference of the parameters of  a bottom-up model for PCR amplification. This model is  developed in Ndifon Wilfred, Hilah Gal, Eric Shifrut, Rina Aharoni, Nissan Yissachar, Nir Waysbort, Shlomit Reich Zeliger, Ruth Arnon, and Nir Friedman (2012), <http://www.pnas.org/content/109/39/15865.full>, and results in a distribution for the counts that is a superposition of the binomial and negative binomial distribution.
	"""
	
	cran = "denoiSeq" 

	version("0.1.1", md5="4c3295a5fa7e33c3090046e1a149c310")

