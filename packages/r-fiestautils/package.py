# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFiestautils(RPackage):
	"""Utility Functions for Forest Inventory Estimation and Analysis

	A set of tools for data wrangling, spatial data analysis,
    statistical modeling (including direct, model-assisted, photo-based, and
    small area tools), and USDA Forest Service data base tools. These tools are
    aimed to help Foresters, Analysts, and Scientists extract and perform
    analyses on USDA Forest Service data.
	"""
	
	homepage = "https://github.com/USDAForestService/FIESTAutils"
	cran = "FIESTAutils" 

	version("1.2.2", md5="6a36562a65a6ebd97ac111574c1dbe72")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-gdalraster", type=("build", "run"))
	depends_on("r-hbsae", type=("build", "run"))
	depends_on("r-josae", type=("build", "run"))
	depends_on("r-mase", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rpostgresql", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-sae", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
