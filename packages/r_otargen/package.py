# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtargen(RPackage):
	"""Access Open Target Genetics

	Interact seamlessly with Open Target Genetics' GraphQL endpoint to query and retrieve tidy data tables, facilitating the analysis of genetic data. For more information about the Open Target Genetics API(<https://genetics.opentargets.org/api>).
	"""
	
	homepage = "https://amirfeizi.github.io/otargen/"
	cran = "otargen" 

	version("1.1.1", md5="60198df73a74177915d50b1ac49d2060")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ghql", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-ggiraphextra", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
