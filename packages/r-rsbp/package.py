# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsbp(RPackage):
	"""Part Information from the Registry of Standard Biological Parts

	Provides an R interface to the Registry of Standard Biological Parts API maintained by the iGEM Foundation: <https://igem.org/Main_Page>. Facilitates retrieval of
    the part number, authorship, date of entry, url, short description, type, and sequence following the guidelines set forth at <http://parts.igem.org/Registry_API/Guidelines>. 
    All Registry content falls under Creative Commons Attribution-ShareAlike: <https://creativecommons.org/licenses/by-sa/4.0/>.
	"""
	
	cran = "rsbp" 

	version("0.1.0", md5="d98d52ee15d7d61e7fb490a875758de9")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.4:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.3:", type=("build", "run"))
