# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhtmult(RPackage):
	"""Multiple Hypotheses Testing for Multiple Families/Groups
Structure

	A Comprehensive tool for almost all existing multiple testing
    methods for multiple families. The package summarizes the existing methods for multiple families multiple testing procedures (MTPs) such as double FDR, group Benjamini-Hochberg (GBH) procedure and average FDR controlling procedure. The package also provides some novel multiple testing procedures using selective inference idea.
	"""
	
	cran = "MHTmult" 

	version("0.1.0", md5="b14bd0e0a69eeedbab83598a0725c411")

