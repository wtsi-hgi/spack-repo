# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatentr(RPackage):
	"""Access USPTO Bulk Data in Tidy Rectangular Format

	Converts TXT and XML data curated by the United States Patent and
    Trademark Office (USPTO). Allows conversion of bulk data after downloading
    directly from the USPTO bulk data website, eliminating need for users to
    wrangle multiple data formats to get large patent databases in tidy,
    rectangular format. Data details can be found on the USPTO website
    <https://bulkdata.uspto.gov/>. Currently, all 3 formats: 1. TXT data
    (1976-2001); 2. XML format 1 data (2002-2004); and 3. XML format 2 data
    (2005-current) can be converted to rectangular, CSV format.
    Relevant literature that uses data from USPTO includes Wada (2020)
    <doi:10.1007/s11192-020-03674-4> and Plaza & Albert (2008)
    <doi:10.1007/s11192-007-1763-3>.
	"""
	
	homepage = "https://JYProjs.github.io/patentr/"
	cran = "patentr" 

	version("0.1.4", md5="c64214cf47ad89a0073f967e90efe3aa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-xml2@1.3.2:", type=("build", "run"))
	depends_on("r-progress@1.2.2:", type=("build", "run"))
