# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLodgwas(RPackage):
	"""Genome-Wide Association Analysis of a Biomarker Accounting for
Limit of Detection

	Genome-wide association (GWAS) analyses
  of a biomarker that account for the limit of detection.
	"""
	
	cran = "lodGWAS" 

	version("1.0-7", md5="e8a7a9b152e9afe6457a43a2577c7dcd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
