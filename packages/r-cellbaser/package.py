# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellbaser(RPackage):
	"""Querying annotation data from the high performance Cellbase web

	This R package makes use of the exhaustive RESTful Web service API that has been implemented for the Cellabase database. It enable researchers to query and obtain a wealth of biological information from a single database saving a lot of time. Another benefit is that researchers can easily make queries about different biological topics and link all this information together as all information is integrated.
	"""
	
	homepage = "https://github.com/melsiddieg/cellbaseR"
	bioc = "cellbaseR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/cellbaseR_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/cellbaseR/cellbaseR_1.26.0.tar.gz"]

	version("1.26.0", md5="1540f788e9e1fba133da3a369fe2c8b4")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
