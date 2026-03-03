# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFortls(RPackage):
	"""Automatic Processing of Terrestrial-Based Technologies Point
Cloud Data for Forestry Purposes

	Process automation of point cloud data derived from terrestrial-based technologies such as Terrestrial Laser Scanner (TLS) or Mobile Laser Scanner. 'FORTLS' enables (i) detection of trees and estimation of tree-level attributes (e.g. diameters and heights), (ii) estimation of stand-level variables (e.g. density, basal area, mean and dominant height), (iii) computation of metrics related to important forest attributes estimated in Forest Inventories at stand-level, and (iv) optimization of plot design for combining TLS data and field measured data. Documentation about 'FORTLS' is described in Molina-Valero et al. (2022, <doi:10.1016/j.envsoft.2022.105337>). 
	"""
	
	homepage = "https://github.com/Molina-Valero/FORTLS"
	cran = "FORTLS" 

	version("1.4.0", md5="ee3cef258879c4851b3b8c73600571b1")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-distance", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lidr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcsf", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-voxr", type=("build", "run"))
	depends_on("r-vroom", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
