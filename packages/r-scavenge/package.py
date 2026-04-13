# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScavenge(RPackage):
	"""Single Cell Analysis of Variant Enrichment through Network propagation.

	SCAVENGE identifies trait-relevant cell types/states at single-cell
	resolution by propagating genetic association signals across cellular
	neighborhood graphs."""

	homepage = "https://github.com/sankaranlab/SCAVENGE"
	git = "https://github.com/sankaranlab/SCAVENGE.git"

	version("20230217", commit="8ee8b173d965009a696b2a590d5b17b28b7cf851")

	depends_on("r@4.0:", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-gchromvar", type=("build", "run"))
