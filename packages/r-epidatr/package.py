# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpidatr(RPackage):
	"""Client for Delphi's 'Epidata' API

	The Delphi 'Epidata' API provides real-time access to epidemiological surveillance data for influenza, 'COVID-19', and other diseases for the USA at various geographical resolutions, both from official government sources such as the Center for Disease Control (CDC) and Google Trends and private partners such as Facebook and Change 'Healthcare'. It is built and maintained by the Carnegie Mellon University Delphi research group. To cite this API: David C. Farrow, Logan C. Brooks, Aaron 'Rumack', Ryan J. 'Tibshirani', 'Roni' 'Rosenfeld' (2015). Delphi 'Epidata' API. <https://github.com/cmu-delphi/delphi-epidata>.
	"""
	
	homepage = "https://cmu-delphi.github.io/epidatr/"
	cran = "epidatr" 

	version("1.0.0", md5="7d3ee0d3a052a9edb62c953d2f4a126b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mmwrweek", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
