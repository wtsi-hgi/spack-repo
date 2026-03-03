# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialdecon(RPackage):
	"""Deconvolution of mixed cells from spatial and/or bulk gene expression data

	Using spatial or bulk gene expression data, estimates abundance of mixed cell types within each observation. Based on "Advances in mixed cell deconvolution enable quantification of cell types in spatial transcriptomic data", Danaher (2022). Designed for use with the NanoString GeoMx platform, but applicable to any gene expression data.
	"""
	
	bioc = "SpatialDecon" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SpatialDecon_1.12.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SpatialDecon/SpatialDecon_1.12.3.tar.gz"]

	version("1.12.3", md5="41ce36a3eeb7683676bb45809eb85730")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-seuratobject", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-geomxtools", type=("build", "run"))
	depends_on("r-repmis", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-lognormreg@0.4:", type=("build", "run"))
