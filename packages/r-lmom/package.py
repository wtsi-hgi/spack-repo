# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmom(RPackage):
	"""L-Moments

	Functions related to L-moments: computation of L-moments
  and trimmed L-moments of distributions and data samples; parameter
  estimation; L-moment ratio diagram; plot vs. quantiles of an
  extreme-value distribution.
	"""
	
	cran = "lmom" 

	version("3.0", md5="01a213710c3f74aff1bc048e771e1f37")

	depends_on("r@3:", type=("build", "run"))
