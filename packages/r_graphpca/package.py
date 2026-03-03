# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphpca(RPackage):
	"""Graphical Tools of Histogram PCA

	Histogram principal components analysis is the generalization of the PCA. Histogram data are adapted to design complex and big data which histograms used as variables (big data adapter). Functions implemented provides numerical and graphical tools of an extension of PCA. Sun Makosso Kallyth (2016) <doi:10.1002/sam.11270>. Sun Makosso Kallyth and Edwin Diday (2012) <doi:10.1007/s11634-012-0108-0>.
	"""
	
	cran = "GraphPCA" 

	version("1.1", md5="483628c86f1e2f9eca74df47bc12e9ca")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-ggplot2movies", type=("build", "run"))
