# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemisup(RPackage):
	"""Semi-Supervised Mixture Model

	Implements a parametric semi-supervised mixture model. The permutation test detects markers with main or interactive effects, without distinguishing them. Possible applications include genome-wide association analysis and differential expression analysis.
	"""
	
	homepage = "https://github.com/rauschenberger/semisup"
	bioc = "semisup"

	version("1.32.0", commit="2559836e843e648dfe09264a5af674fa5377cbdf")
	version("1.26.0", commit="59f2b128e003a64a260ad027281185a6ca5b2667")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
