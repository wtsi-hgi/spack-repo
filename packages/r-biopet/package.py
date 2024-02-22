# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiopet(RPackage):
	"""Biomarker Prognostic Enrichment Tool

	Prognostic Enrichment is a clinical trial strategy of evaluating an intervention in a patient population with a higher rate of the unwanted event than the broader patient population (R. Temple (2010) <DOI:10.1038/clpt.2010.233>). A higher event rate translates to a lower sample size for the clinical trial, which can have both practical and ethical advantages. This package is a tool to help evaluate biomarkers for prognostic enrichment of clinical trials. 
	"""
	
	cran = "BioPET" 

	version("0.2.2", md5="c6eecbfa032a7e63f23a6aebc9fe8ddd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
