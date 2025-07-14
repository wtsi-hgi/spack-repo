# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancerunt(RPackage):
	"""Gene expression dataset published by Sotiriou et al. [2007] (UNT).

	Gene expression data from a breast cancer study published by Sotiriou et al. in 2007, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerUNT"

	version("1.46.0", commit="126eb96c0db9af633311216333ecb01d47009b71")
	version("1.40.0", commit="7793740110fe7d95b590c093df752e3250e310f8")

	depends_on("r@2.5:", type=("build", "run"))

