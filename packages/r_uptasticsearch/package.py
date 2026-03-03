# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUptasticsearch(RPackage):
	"""Get Data Frame Representations of 'Elasticsearch' Results

	
    'Elasticsearch' is an open-source, distributed, document-based datastore
    (<https://www.elastic.co/products/elasticsearch>).
    It provides an 'HTTP' 'API' for querying the database and extracting datasets, but that
    'API' was not designed for common data science workflows like pulling large batches of
    records and normalizing those documents into a data frame that can be used as a training
    dataset for statistical models. 'uptasticsearch' provides an interface for 'Elasticsearch'
    that is explicitly designed to make these data science workflows easy and fun.
	"""
	
	homepage = "https://github.com/uptake/uptasticsearch"
	cran = "uptasticsearch" 

	version("0.4.0", md5="0b257d3592ca391a1cc1be744da45443")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
