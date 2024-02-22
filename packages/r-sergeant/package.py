# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSergeant(RPackage):
	"""Tools to Transform and Query Data with Apache Drill

	Apache Drill is a low-latency distributed query engine designed to enable 
    data exploration and analysis on both relational and non-relational data stores, 
    scaling to petabytes of data. Methods are provided that enable working with Apache 
    Drill instances via the REST API, DBI methods
    and using 'dplyr'/'dbplyr' idioms. Helper functions are included to facilitate
    using official Drill Docker images/containers.
	"""
	
	homepage = "https://gitlab.com/hrbrmstr/sergeant"
	cran = "sergeant" 

	version("0.9.1", md5="94fa4ccd67ff199dffd5d23cedce080f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bit64@0.9.7:", type=("build", "run"))
	depends_on("r-dbi@0.7:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-dbplyr@1.3:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
