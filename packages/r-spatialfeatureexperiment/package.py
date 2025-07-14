# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialfeatureexperiment(RPackage):
	"""Integrating SpatialExperiment with Simple Features in sf

	A new S4 class integrating Simple Features with the R package sf to bring geospatial data analysis methods based on vector data to spatial transcriptomics. Also implements management of spatial neighborhood graphs and geometric operations. This pakage builds upon SpatialExperiment and SingleCellExperiment, hence methods for these parent classes can still be used.
	"""
	
	homepage = "https://github.com/pachterlab/SpatialFeatureExperiment"
	bioc = "SpatialFeatureExperiment" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SpatialFeatureExperiment_1.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SpatialFeatureExperiment/SpatialFeatureExperiment_1.4.0.tar.gz"]

    version("1.10.1", tag="RELEASE_3_21")
	version("1.4.0", sha256="a67f7c39bd846a69fbd661a6b3f72648cd4e6ac553e75d925fec6256d5cc47fb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biocneighbors", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-spdep@1.1.7:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
