# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArdeco(RPackage):
	"""'ARDECO' Dataset

	A set of functions to access the 'ARDECO' (Annual Regional Database
    of the European Commission) data directly from the official ARDECO public
    repository through the exploitation of the 'ARDECO' APIs.
    The APIs are completely transparent to the user and the provided functions
    provide a direct access to the 'ARDECO' data.
    The 'ARDECO' database is a collection of variables related to demography,
    employment, labour market, domestic product, capital formation.
    Each variable can be exposed in one or more units of measure as well as
    refers to total values plus economic sectors.
    The description of the 'ARDECO' database can be found at the following URL
    <https://urban.jrc.ec.europa.eu/ardeco>.
	"""
	
	cran = "ARDECO" 

	version("0.1.1", md5="6ef365956fdeadc46b77e41d33bb79c8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ghql", type=("build", "run"))
	depends_on("r-rjstat", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
