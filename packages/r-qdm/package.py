# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQdm(RPackage):
	"""Fitting a Quadrilateral Dissimilarity Model to Same-Different
Judgments

	This package provides different specifications of a Quadrilateral
    Dissimilarity Model which can be used to fit same-different judgments
    in order to get a predicted matrix that satisfies regular minimality
    [Colonius & Dzhafarov, 2006, Measurement and representations of
    sensations, Erlbaum]. From such a matrix, Fechnerian distances can be
    computed.
	"""
	
	cran = "qdm" 

	version("0.1-0", md5="991c1b4cf966d435b11aa8a78a83cde0")

	depends_on("r@3.1:", type=("build", "run"))
