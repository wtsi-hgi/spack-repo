# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskmetric(RPackage):
	"""Risk Metrics to Evaluating R Packages

	Facilities for assessing R packages against a number of metrics to 
    help quantify their robustness.
	"""
	
	homepage = "https://pharmar.github.io/riskmetric/"
	cran = "riskmetric" 

	version("0.2.4", md5="bde9f5b4579b7a76f5357f0d7813fbea")

	depends_on("r-backports", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-cranlogs", type=("build", "run"))
	depends_on("r-covr", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-pkgload", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
