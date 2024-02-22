# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecomposer(RPackage):
	"""Empirical Mode Decomposition for Cyclostratigraphy

	Tools to apply Ensemble Empirical Mode 
    Decomposition (EEMD) for cyclostratigraphy purposes. Mainly: a new 
    algorithm, extricate, that performs EEMD in seconds, a linear interpolation 
    algorithm  using the greatest rational common divisor of depth or time, 
    different algorithms to compute instantaneous amplitude, frequency and  
    ratios of frequencies, and functions to verify and visualise the outputs.
    The functions were developed during the CRASH project (Checking the 
    Reproducibility of Astrochronology in the Hauterivian). When using for 
    publication please cite Wouters, S., Crucifix, M., Sinnesael, M., Da Silva, 
    A.C., Zeeden, C., Zivanovic, M., Boulvain, F., Devleeschouwer, X., 2022, 
    "A decomposition approach to cyclostratigraphic signal processing". 
    Earth-Science Reviews 225 (103894).
    <doi:10.1016/j.earscirev.2021.103894>.
	"""
	
	cran = "DecomposeR" 

	version("1.0.6", md5="d9f445c2e528d4ebaf84c251990e15b9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-tictoc", type=("build", "run"))
	depends_on("r-stratigrapher@1.1.1:", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
