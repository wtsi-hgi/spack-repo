# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpendatatoronto(RPackage):
	"""Access the City of Toronto Open Data Portal

	Access data from the "City of Toronto
    Open Data Portal" (<https://open.toronto.ca>) directly from R.
	"""
	
	homepage = "https://sharlagelfand.github.io/opendatatoronto/"
	cran = "opendatatoronto" 

	version("0.1.5", md5="84a12a325215f233190f9db2861649e5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ckanr@0.6:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
