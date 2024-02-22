# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenml(RPackage):
	"""Open Machine Learning and Open Data Platform

	We provide an R interface to 'OpenML.org' which is an online machine learning platform where researchers can access open data, download and upload data sets, share their machine learning tasks and experiments and organize them online to work and collaborate with other researchers. 
    The R interface allows to query for data sets with specific properties, and allows the downloading and uploading of data sets, tasks, flows and runs. 
    See <https://www.openml.org/guide/api> for more information.
	"""
	
	homepage = "https://github.com/openml/openml-r"
	cran = "OpenML" 

	version("1.12", md5="5d2adbbf986ef0f48b46e70fb40768c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-backports@1.1:", type=("build", "run"))
	depends_on("r-bbmisc@1.11:", type=("build", "run"))
	depends_on("r-checkmate@1.8.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise@1:", type=("build", "run"))
	depends_on("r-curl@4.1:", type=("build", "run"))
