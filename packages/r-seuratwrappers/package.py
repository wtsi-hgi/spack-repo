# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeuratwrappers(RPackage):
	"""SeuratWrappers is a collection of community-provided methods and extensions for Seurat, curated by the Satija Lab at NYGC. These methods comprise functionality not presently found in Seurat, and are able to be updated much more frequently."""

	homepage = "https://github.com/satijalab/seurat-wrappers"
	git = "https://github.com/satijalab/seurat-wrappers.git"

	# Recent snapshot (compatible with Seurat 5)
	version("2024-01-29", commit="d9594f67a9eab4f917390010a1c106b5422b102e", preferred=True)
	# Older snapshot; still requires Seurat 5
	version("2023-07-20", commit="91c5c3ffb0aa951e73108a53b36260019f2c10d8")
	# Legacy snapshot compatible with Seurat 3/4
	version("2020-09-29", commit="79fe9001d8bba43d10caf7c98fb0b2784b6f1dce")

	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	# Match Seurat major versions across snapshots
	depends_on("r-seurat@5:", type=("build", "run"), when="@2024-01-29")
	depends_on("r-seurat@5:", type=("build", "run"), when="@2023-07-20")
	depends_on("r-seurat@3:", type=("build", "run"), when="@2020-09-29")
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
