# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTtscreening(RPackage):
	"""Genome-Wide DNA Methylation Sites Screening by Use of Training
and Testing Samples

	A screening process utilizing training and testing samples to filter out uninformative DNA methylation sites. Surrogate variables (SVs) of DNA methylation are included in the filtering process to explain unknown factor effects. 
	"""
	
	cran = "ttScreening" 

	version("1.6", md5="af2bd174aefe7408522513002b1149cd")

	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-simsalapar", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
