# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskyr(RPackage):
	"""Rendering Risk Literacy more Transparent

	Risk-related information (like the prevalence of conditions, the sensitivity and specificity of diagnostic tests, or the effectiveness of interventions or treatments) can be expressed in terms of frequencies or probabilities. By providing a toolbox of corresponding metrics and representations, 'riskyr' computes, translates, and visualizes risk-related information in a variety of ways. Adopting multiple complementary perspectives provides insights into the interplay between key parameters and renders teaching and training programs on risk literacy more transparent. 
	"""
	
	homepage = "https://riskyr.org/"
	cran = "riskyr" 

	version("0.4.0", md5="1601eaf1058a3f70f5b5d73a079a22e9")

	depends_on("r@3.4:", type=("build", "run"))
