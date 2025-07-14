# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowclust(RPackage):
	"""Clustering for Flow Cytometry

	Robust model-based clustering using a t-mixture model with Box-Cox transformation. Note: users should have GSL installed. Windows users: 'consult the README file available in the inst directory of the source distribution for necessary configuration instructions'.
	"""
	
	bioc = "flowClust"

	version("3.46.0", commit="a682d03c974dc5fce818d269f18b8a03fed92a74")
	version("3.40.0", commit="4acf935093c75e3ba927715688f3c9af8519af36")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
