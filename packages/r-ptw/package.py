# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtw(RPackage):
	"""Parametric Time Warping.

	Parametric Time Warping aligns patterns, i.e. it aims to put corresponding
	features at the same locations. The algorithm searches for an optimal
	polynomial describing the warping. It is possible to align one sample to a
	reference, several samples to the same reference, or several samples to
	several references. One can choose between calculating individual warpings,
	or one global warping for a set of samples and one reference. Two
	optimization criteria are implemented: RMS (Root Mean Square error) and WCC
	(Weighted Cross Correlation). Both warping of peak profiles and of peak
	lists are supported. A vignette for the latter is contained in the inst/doc
	directory of the source package - the vignette source can be found on the
	package github site."""

	cran = "ptw"

	license("GPL-2.0-or-later")

	version("1.9-16", md5="8b2fcbe360807dce7ac1b0f012b10cad")

	depends_on("r-rcppde", type=("build", "run"))
