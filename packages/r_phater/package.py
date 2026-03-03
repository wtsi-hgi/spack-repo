# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhater(RPackage):
	"""PHATE - Potential of Heat-Diffusion for Affinity-Based
Transition Embedding

	PHATE is a tool for visualizing high dimensional single-cell data
  with natural progressions or trajectories. PHATE uses a novel conceptual framework
  for learning and visualizing the manifold inherent to biological systems in which
  smooth transitions mark the progressions of cells from one state to another.
  To see how PHATE can be applied to single-cell RNA-seq datasets from hematopoietic
  stem cells, human embryonic stem cells, and bone marrow samples, check out our publication in Nature Biotechnology
  at <doi:10.1038/s41587-019-0336-3>.
	"""
	
	cran = "phateR" 

	version("1.0.7", md5="3aa06a68d099edcff7a84ed1e2ac33c3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix@1.2.0:", type=("build", "run"))
	depends_on("r-reticulate@1.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
