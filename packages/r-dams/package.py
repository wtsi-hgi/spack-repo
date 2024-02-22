# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDams(RPackage):
	"""Dams in the United States from the National Inventory of Dams
(NID)

	The single largest source of dams in the United States is the
    National Inventory of Dams (NID) <http://nid.usace.army.mil> from the US
    Army Corps of Engineers. Entire data from the NID cannot be obtained all at
    once and NID's website limits extraction of more than a couple of thousand
    records at a time. Moreover, selected data from the NID's user interface
    cannot not be saved to a file. In order to make the analysis of this data
    easier, all the data from NID was extracted manually. Subsequently, the raw
    data was checked for potential errors and cleaned. This package provides
    sample cleaned data from the NID and provides functionality to access the
    entire cleaned NID data.
	"""
	
	homepage = "https://github.com/jsta/dams"
	cran = "dams" 

	version("0.3.0", md5="7bad6ecb967000c42252f83fc8bc23cb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-fauxpas", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
