# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparklyr(RPackage):
	"""R Interface to Apache Spark

	R interface to Apache Spark, a fast and general
    engine for big data processing, see <https://spark.apache.org/>. This
    package supports connecting to local and remote Apache Spark clusters,
    provides a 'dplyr' compatible back-end, and provides an interface to
    Spark's built-in machine learning algorithms.
	"""
	
	homepage = "https://spark.rstudio.com/"
	cran = "sparklyr" 

	version("1.8.4", md5="cede2e204859454506b8d6069c24bce7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-config@0.2:", type=("build", "run"))
	depends_on("r-dbi@1:", type=("build", "run"))
	depends_on("r-dbplyr@2.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.4:", type=("build", "run"))
	depends_on("r-openssl@0.8:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@0.1.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.10:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("spark@1.6:", type=("build", "link", "run"))
