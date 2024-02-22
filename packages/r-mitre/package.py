# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMitre(RPackage):
	"""Cybersecurity MITRE Standards Data and Digraphs

	Extract, transform and load MITRE standards.
    This package gives you an approach to cybersecurity data sets.
    All data sets are build on runtime downloading raw data from MITRE public services.
    MITRE <https://www.mitre.org/> is a government-funded research organization 
    based in Bedford and McLean. Current version includes most used standards as
    data frames. It also provide a list of nodes and edges with all relationships.
	"""
	
	homepage = "https://github.com/motherhack3r/mitre"
	cran = "mitre" 

	version("1.0.0", md5="4ea15f640ba15d951f169a45ea5f3925")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
