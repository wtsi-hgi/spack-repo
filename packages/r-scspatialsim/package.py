# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScspatialsim(RPackage):
	"""A Point Pattern Simulator for Spatial Cellular Data

	Single cell resolution data has been valuable in learning about tissue microenvironments and interactions between cells or spots. This package allows for the simulation of this level of data, be it single cell or ‘spots’, in both a univariate (single metric or cell type) and bivariate (2 or more metrics or cell types) ways. As more technologies come to marker, more methods will be developed to derive spatial metrics from the data which will require a way to benchmark methods against each other. Additionally, as the field currently stands, there is not a gold standard method to be compared against. We set out to develop an R package that will allow users to simulate point patterns that can be biologically informed from different tissue domains, holes, and varying degrees of clustering/colocalization. The data can be exported as spatial files and a summary file (like 'HALO'). <https://github.com/FridleyLab/scSpatialSIM/>.
	"""
	
	homepage = "https://github.com/FridleyLab/scSpatialSIM"
	cran = "scSpatialSIM" 

	version("0.1.3.3", md5="7461e0cdb88d6ebaa7d8238804aeaee1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
