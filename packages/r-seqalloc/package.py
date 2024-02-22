# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqalloc(RPackage):
	"""Sequential Allocation for Prospective Experiments

	Potential randomization schemes are prospectively evaluated when
    units are assigned to treatment arms upon entry into the experiment. The schemes
    are evaluated for balance on covariates and on predictability (i.e., how well
    could a site worker guess the treatment of the next unit enrolled).
	"""
	
	cran = "SeqAlloc" 

	version("1.0", md5="80a2865cfbaf5e46edcecd0146a724e9")

