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

	version("1.32.0", commit="f1c044414d4beab4fd27e7d2a269033be7f63c34")
	version("1.26.0", commit="0c5400a13f306d6fa40c1f3bf0de326f2735c229")

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
