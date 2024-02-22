# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInformation(RPackage):
	"""Data Exploration with Information Theory (Weight-of-Evidence and
Information Value)

	Performs exploratory data analysis and variable screening for
    binary classification models using weight-of-evidence (WOE) and information
    value (IV). In order to make the package as efficient as possible, aggregations
    are done in data.table and creation of WOE vectors can be distributed across
    multiple cores. The package also supports exploration for uplift models (NWOE
    and NIV).
	"""
	
	cran = "Information" 

	version("0.0.9", md5="24d8c459cb2df65e6d588ea477278991")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
