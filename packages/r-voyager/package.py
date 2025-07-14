# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVoyager(RPackage):
	"""From geospatial to spatial omics

	SpatialFeatureExperiment (SFE) is a new S4 class for working with spatial single-cell genomics data. The voyager package implements basic exploratory spatial data analysis (ESDA) methods for SFE. Univariate methods include univariate global spatial ESDA methods such as Moran's I, permutation testing for Moran's I, and correlograms. Bivariate methods include Lee's L and cross variogram. Multivariate methods include MULTISPATI PCA and multivariate local Geary's C recently developed by Anselin. The Voyager package also implements plotting functions to plot SFE data and ESDA results.
	"""
	
	homepage = "https://github.com/pachterlab/voyager"
	bioc = "Voyager" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Voyager_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Voyager/Voyager_1.4.0.tar.gz"]

    version("1.10.0", tag="RELEASE_3_21")
	version("1.4.0", sha256="e04a6570a1b15319841d68946f59a9f9296b52c0776200a68663313ff447f538")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bluster", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-scico", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-spatialfeatureexperiment@1.2.1:", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
