# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedcapapi(RPackage):
	"""Interface to 'REDCap'

	Access data stored in 'REDCap' databases using the Application
    Programming Interface (API).  'REDCap' (Research Electronic Data CAPture;
    <https://projectredcap.org>, Harris, et al. (2009) <doi:10.1016/j.jbi.2008.08.010>, 
    Harris, et al. (2019) <doi:10.1016/j.jbi.2019.103208>) is
    a web application for building and managing online surveys and databases
    developed at Vanderbilt University.  The API allows users to access data
    and project meta data (such as the data dictionary) from the web
    programmatically. The 'redcapAPI' package facilitates the process of
    accessing data with options to prepare an analysis-ready data set
    consistent with the definitions in a database's data dictionary.
	"""
	
	homepage = "https://github.com/vubiostat/redcapAPI"
	cran = "redcapAPI" 

	version("2.8.4", md5="0def80db18ecd45e41f6f54d2369bfea")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-labelvector", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
