# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancertransbig(RPackage):
	"""Gene expression dataset published by Desmedt et al. [2007] (TRANSBIG).

	Gene expression data from a breast cancer study published by Desmedt et al. in 2007, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerTRANSBIG"

	version("1.46.0", commit="9d994b70be911209dc1e0775d1f0ef79490402ae")
	version("1.40.0", commit="cd416ca135e47e5f554fd739f98d55520de45647")

	depends_on("r@2.5:", type=("build", "run"))

