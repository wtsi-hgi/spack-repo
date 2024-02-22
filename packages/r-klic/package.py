# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlic(RPackage):
	"""Kernel Learning Integrative Clustering

	Kernel Learning Integrative Clustering (KLIC) is an algorithm that allows to combine multiple kernels, each representing a different measure of the similarity between a set of observations. The contribution of each kernel on the final clustering is weighted according to the amount of information carried by it. As well as providing the functions required to perform the kernel-based clustering, this package also allows the user to simply give the data as input: the kernels are then built using consensus clustering. Different strategies to choose the best number of clusters are also available. For further details please see Cabassi and Kirk (2020) <doi:10.1093/bioinformatics/btaa593>.
	"""
	
	homepage = "http://github.com/acabassi/klic"
	cran = "klic" 

	version("1.0.4", md5="42025b385eba4109d3065a7608d839bc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-coca", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
