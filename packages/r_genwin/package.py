# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenwin(RPackage):
	"""Spline Based Window Boundaries for Genomic Analyses

	Defines window or bin boundaries for the analysis of genomic data.
    Boundaries are based on the inflection points of a cubic smoothing spline
    fitted to the raw data. Along with defining boundaries, a technique to
    evaluate results obtained from unequally-sized windows is provided.
    Applications are particularly pertinent for, though not limited to, genome
    scans for selection based on variability between populations (e.g. using
    Wright's fixations index, Fst, which measures variability in subpopulations
    relative to the total population).
	"""
	
	cran = "GenWin" 

	version("1.0", md5="9699f793ccd903750aa2c3b5643fcf6c")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-pspline", type=("build", "run"))
