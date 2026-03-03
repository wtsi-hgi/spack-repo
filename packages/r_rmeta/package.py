# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmeta(RPackage):
	"""Meta-Analysis

	Functions for simple fixed and random effects
        meta-analysis for two-sample comparisons and cumulative
        meta-analyses. Draws standard summary plots, funnel plots, and
        computes summaries and tests for association and heterogeneity.
	"""
	
	cran = "rmeta" 

	version("3.0", md5="b14aa174ad5bb7b8abb413a5aa4eacc0")

