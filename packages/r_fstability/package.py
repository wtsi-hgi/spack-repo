# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFstability(RPackage):
	"""Calculate Feature Stability

	Has two functions to help with calculating feature selection stability. 'Lump' is a function that groups subset vectors into a dataframe, and adds NA to shorter vectors so they all have the same length.
    'ASM' is a function that takes a dataframe of subset vectors and the original vector of features as inputs, and calculates the Stability of the feature selection.
    The calculation for 'asm' uses the Adjusted Stability Measure proposed in: 'Lustgarten', 'Gopalakrishnan', & 'Visweswaran' (2009)<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2815476/>.
	"""
	
	cran = "Fstability" 

	version("0.1.2", md5="a0f9b4fdb07aef1600c0f7ccd8ffe81f")

