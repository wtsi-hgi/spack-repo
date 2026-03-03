# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFdrestimation(RPackage):
	"""Estimate, Plot, and Summarize False Discovery Rates

	The user can directly compute and display false discovery rates from inputted p-values or z-scores under a variety of assumptions. p.fdr() computes FDRs, adjusted p-values and decision reject vectors from inputted p-values or z-values. get.pi0() estimates the proportion of data that are truly null. plot.p.fdr() plots the FDRs, adjusted p-values, and the raw p-values points against their rejection threshold lines.  
	"""
	
	homepage = "<doi:10.12688/f1000research.52999.2>"
	cran = "FDRestimation" 

	version("1.0.1", md5="040a0a6200ca010eab5e6837864ed570")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
