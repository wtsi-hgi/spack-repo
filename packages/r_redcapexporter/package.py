# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedcapexporter(RPackage):
	"""Automated Construction of R Data Packages from REDCap Projects

	Export all data, including metadata, from a REDCap (Research
    Electronic Data Capture) Project via the REDCap API
    <https://projectredcap.org/wp-content/resources/REDCapTechnicalOverview.pdf>.
    The exported (meta)data will be processed and formatted into a stand alone R
    data package which can be installed and shared between researchers.  Several
    default reports are generated as vignettes in the resulting package.
	"""
	
	homepage = "https://github.com/dewittpe/REDCapExporter"
	cran = "REDCapExporter" 

	version("0.2.2", md5="ea724d30a685e8b31527e2f14863473a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
