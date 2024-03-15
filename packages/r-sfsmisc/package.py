# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfsmisc(RPackage):
	"""Utilities from 'Seminar fuer Statistik' ETH Zurich.

	Useful utilities ['goodies'] from Seminar fuer Statistik ETH Zurich, some
	of which were ported from S-plus in the 1990s.; For graphics, have pretty
	(Log-scale) axes, an enhanced Tukey-Anscombe plot, combining histogram and
	boxplot, 2d-residual plots, a 'tachoPlot()', pretty arrows, etc.; For
	robustness, have a robust F test and robust range().; For system support,
	notably on Linux, provides 'Sys.*()' functions with more access to system
	and CPU information.; Finally, miscellaneous utilities such as simple
	efficient prime numbers, integer codes, Duplicated(), toLatex.numeric() and
	is.whole()."""

	cran = "sfsmisc"

	license("GPL-2.0-or-later")

	version("1.1-17", md5="64b3bdc77274ba039f0229135b9290ea")

	depends_on("r@3.3:", type=("build", "run"))
