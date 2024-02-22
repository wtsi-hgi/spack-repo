# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultitaper(RPackage):
	"""Spectral Analysis Tools using the Multitaper Method.

	Implements multitaper spectral analysis using discrete prolate spheroidal
	sequences (Slepians) and sine tapers. It includes an adaptive weighted
	multitaper spectral estimate, a coherence estimate, Thomson's Harmonic
	F-test, and complex demodulation. The Slepians sequences are generated
	efficiently using a tridiagonal matrix solution, and jackknifed confidence
	intervals are available for most estimates. This package is an
	implementation of the method described in D.J. Thomson (1982) "Spectrum
	estimation and harmonic analysis" <doi:10.1109/PROC.1982.12433>."""

	cran = "multitaper"

	version("1.0-17", md5="b06203f832564a39ecea719b2d006771")

	depends_on("r@3:", type=("build", "run"))
