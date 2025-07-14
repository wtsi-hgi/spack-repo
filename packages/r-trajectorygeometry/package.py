# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrajectorygeometry(RPackage):
	"""This Package Discovers Directionality in Time and Pseudo-times Series of Gene Expression Patterns

	Given a time series or pseudo-times series of gene expression data, we might wish to know: Do the changes in gene expression in these data exhibit directionality?  Are there turning points in this directionality.  Do different subsets of the data move in different directions?  This package uses spherical geometry to probe these sorts of questions.  In particular, if we are looking at (say) the first n dimensions of the PCA of gene expression, directionality can be detected as the clustering of points on the (n-1)-dimensional sphere.
	"""
	
	bioc = "TrajectoryGeometry" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TrajectoryGeometry_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TrajectoryGeometry/TrajectoryGeometry_1.10.1.tar.gz"]

	version("1.16.0", tag="RELEASE_3_21")
	version("1.10.1", sha256="4d6fd3d359e7073b69b24d8c6674fa91e8bd3d1910362016ed725d039d638f86")
	version("1.10.0", md5="a955410c20ec9cbae97e2d60a8c9b46f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
