# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbioinf(RPackage):
	"""RBioinf

	Functions and datasets and examples to accompany the monograph R For Bioinformatics.
	"""
	
	bioc = "RBioinf"

	version("1.68.0", commit="4812408628b8d859e20ac82adfa06ff77dda5699")
	version("1.62.0", commit="af88008375506663bca4844a8c3360f0f3d7b76f")

	depends_on("r-graph", type=("build", "run"))
