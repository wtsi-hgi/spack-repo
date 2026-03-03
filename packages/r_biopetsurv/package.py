# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiopetsurv(RPackage):
	"""Biomarker Prognostic Enrichment Tool for Time-to-Event Trial

	Prognostic Enrichment is a strategy of enriching a clinical trial for testing an intervention intended to prevent or delay an unwanted clinical event.  A prognostically enriched trial enrolls only patients who are more likely to experience the unwanted clinical event than the broader patient population (R. Temple (2010) <doi:10.1038/clpt.2010.233>). By testing the intervention in an enriched study population, the trial may be adequately powered with a smaller sample size, which can have both practical and ethical advantages.
    This package provides tools to evaluate biomarkers for prognostic enrichment of clinical trials with survival/time-to-event outcomes.
	"""
	
	cran = "BioPETsurv" 

	version("0.1.0", md5="86e0949032e2f018f509bffa0d48919e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
