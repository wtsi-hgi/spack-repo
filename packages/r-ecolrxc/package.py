# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcolrxc(RPackage):
	"""Ecological Inference of RxC Tables by Latent Structure
Approaches

	Estimates RxC (R by C) vote transfer matrices (ecological contingency tables) from aggregate data building on Thomsen (1987) and Park (2008) approaches.
   References:
   Park, W.-H. (2008). ''Ecological Inference and Aggregate Analysis of Election''. PhD Dissertation. University of Michigan. <https://deepblue.lib.umich.edu/bitstream/handle/2027.42/58525/wpark_1.pdf>
   Thomsen, S.R. (1987, ISBN:87-7335-037-2). ''Danish Elections 1920 79: a Logit Approach to Ecological Analysis and Inference''. Politica, Aarhus, Denmark.
	"""
	
	cran = "ecolRxC" 

	version("0.1.1-10", md5="68eb269dbf555905816cabb3a8523e42")

