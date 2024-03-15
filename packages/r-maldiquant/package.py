# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaldiquant(RPackage):
	"""Quantitative Analysis of Mass Spectrometry Data.

	A complete analysis pipeline for matrix-assisted laser
	desorption/ionization-time-of-flight (MALDI-TOF) and other two-dimensional
	mass spectrometry data. In addition to commonly used plotting and
	processing methods it includes distinctive features, namely baseline
	subtraction methods such as morphological filters (TopHat) or the
	statistics-sensitive non-linear iterative peak-clipping algorithm (SNIP),
	peak alignment using warping functions, handling of replicated measurements
	as well as allowing spectra with different resolutions."""

	cran = "MALDIquant"

	version("1.22.2", md5="389460254c436902b8d8d0980dc805b6")

	depends_on("r@4:", type=("build", "run"))
