# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeuratwrappers(RPackage):
	"""SeuratWrappers is a collection of community-provided methods and extensions for Seurat, curated by the Satija Lab at NYGC. These methods comprise functionality not presently found in Seurat, and are able to be updated much more frequently."""

	homepage = "https://github.com/satijalab/seurat-wrappers"
	git = "https://github.com/satijalab/seurat-wrappers.git"

	version("2024-01-29", commit="d9594f67a9eab4f917390010a1c106b5422b102e")

	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
