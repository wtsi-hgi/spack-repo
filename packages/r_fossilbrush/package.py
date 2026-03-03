# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFossilbrush(RPackage):
	"""Automated Cleaning of Fossil Occurrence Data

	Functions to automate the detection and resolution of taxonomic and stratigraphic errors in fossil occurrence datasets. Functions were developed using data from the Paleobiology Database.
	"""
	
	homepage = "https://cran.r-project.org/package=fossilbrush"
	cran = "fossilbrush" 

	version("1.0.3", md5="eebe738e56df079f0242849682c257bd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
