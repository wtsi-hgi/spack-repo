# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNose(RPackage):
	"""nose Package for R

	The nose package consists of a collection of three
        functions for classifying sparseness in typical 2 x 2 data sets
        with at least one cell should have zero count. These functions
        are based on the three widely applied summary measures for 2 x
        2 categorical data viz, Risk Difference (RD), Relative Risk
        (RR), Odds Ratio (OR). This package helps to identify suitable
        continuity correction for zero cells when a multi centre
        analysis or a meta analysis is carried out. Further, it can be
        considered as a tool for sensitivity analysis for adding a
        continuity correction and to identify the presence of Simpson's
        paradox.
	"""
	
	cran = "nose" 

	version("1.0", md5="88cd4f2696a9f60bb95d0214790f5f29")

