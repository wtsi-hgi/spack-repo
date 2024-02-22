# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiptest(RPackage):
	"""Hartigan's Dip Test Statistic for Unimodality - Corrected.

	Compute Hartigan's dip test statistic for unimodality /; multimodality and
	provide a test with simulation based p-values,  where; the original public
	code has been corrected."""

	cran = "diptest"

	version("0.77-0", md5="f7229b4ba1ca5ad70d996ce984329d73")

