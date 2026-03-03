# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDvhmetrics(RPackage):
	"""Analyze Dose-Volume Histograms and Check Constraints

	Functionality for analyzing dose-volume histograms (DVH)
        in radiation oncology: Read DVH text files, calculate DVH
        metrics as well as generalized equivalent uniform dose (gEUD),
        biologically effective dose (BED), equivalent dose in 2 Gy
        fractions (EQD2), normal tissue complication probability
        (NTCP), and tumor control probability (TCP). Show DVH
        diagrams, check and visualize quality assurance constraints
        for the DVH. Includes web-based graphical user interface.
	"""
	
	homepage = "https://github.com/dwoll/DVHmetrics/"
	cran = "DVHmetrics" 

	version("0.4.2", md5="01af11dc39ad8566e08a0edd79f63f73")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
