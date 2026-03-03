# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinch(RPackage):
	"""Parse Darwin Core Files

	Parse and create Darwin Core (<http://rs.tdwg.org/dwc/>) Simple
    and Archives. Functionality includes reading and parsing all the
    files in a Darwin Core Archive, including the datasets and metadata;
    read and parse simple Darwin Core files; and validation of Darwin
    Core Archives.
	"""
	
	homepage = "https://docs.ropensci.org/finch/"
	cran = "finch" 

	version("0.4.0", md5="8d55cac849167a8b5f5588f5bfe6a0e3")

	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-eml@2:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-hoardr@0.2:", type=("build", "run"))
