# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFloodfreqplot(RPackage):
	"""Flood Probability Plotting and Graphical Frequency Analysis

	Plotting flood quantiles and their corresponding probabilities (return periods) on the probability papers.
    The details of relevant methods are available in Chow et al (1988, ISBN: 007070242X, 9780070702424), and
    Bobee and Ashkar (1991, ISBN: 0918334683, 9780918334688).
	"""
	
	cran = "FloodFreqPlot" 

	version("0.1.0", md5="5ec4ac31f28e62e49c7f1c00559e0321")

	depends_on("r@3.5:", type=("build", "run"))
