# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROntologics(RPackage):
	"""Code-Logics to Handle Ontologies

	Provides tools to build and work with an ontology of linked (open) 
    data in a tidy workflow. It is inspired by the Food and Agrilculture 
    Organizations (FAO) caliper platform 
    <https://www.fao.org/statistics/caliper/web/> and 
    makes use of the Simple Knowledge Organisation System (SKOS).
	"""
	
	homepage = "https://github.com/luckinet/ontologics"
	cran = "ontologics" 

	version("0.7.0", md5="9202433a4e050a818ecb2e9e94d39743")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rdflib", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-beepr", type=("build", "run"))
