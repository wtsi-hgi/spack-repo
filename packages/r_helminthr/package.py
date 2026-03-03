# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelminthr(RPackage):
	"""Access London Natural History Museum Host-Helminth Record
Database

	Access to large host-parasite data is often hampered by the 
  availability of data and difficulty in obtaining it in a programmatic way
  to encourage analyses. 'helminthR' provides a programmatic interface to the 
  London Natural History Museum's host-parasite database, one of the largest 
  host-parasite databases existing currently <https://www.nhm.ac.uk/research-curation/scientific-resources/taxonomy-systematics/host-parasites/>. The package allows the user
  to query by host species, parasite species, and geographic location.
	"""
	
	homepage = "https://docs.ropensci.org/helminthR/"
	cran = "helminthR" 

	version("1.0.10", md5="01619859bb58e8b2dad7c302e9cb6adf")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
