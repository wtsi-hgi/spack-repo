# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIatscores(RPackage):
	"""Implicit Association Test Scores Using Robust Statistics

	Compute several variations of the Implicit Association Test (IAT) scores, including the D scores (Greenwald, Nosek, Banaji, 2003, <doi:10.1037/0022-3514.85.2.197>) and the new scores that were developed using robust statistics (Richetin, Costantini, Perugini, and Schonbrodt, 2015, <doi:10.1371/journal.pone.0129601>). 
	"""
	
	cran = "IATscores" 

	version("0.2.7", md5="ca7c129347274c0760523be7cfec31bd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-qgraph@1.6.5:", type=("build", "run"))
