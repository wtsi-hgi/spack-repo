# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmbedsom(RPackage):
	"""Fast Embedding Guided by Self-Organizing Map

	Provides a smooth mapping of multidimensional points into
    low-dimensional space defined by a self-organizing map. Designed to work
    with 'FlowSOM' and flow-cytometry use-cases. See Kratochvil et al. (2019)
    <doi:10.12688/f1000research.21642.1>.
	"""
	
	homepage = "https://github.com/exaexa/EmbedSOM"
	cran = "EmbedSOM" 

	version("2.1.2", md5="fe9db18739549e413fc80f9cbc100245")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rtsne", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
