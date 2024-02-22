# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdml(RPackage):
	"""Importing Real-Time Thermo Cycler (qPCR) Data from RDML Format
Files

	Imports real-time thermo cycler (qPCR) data from Real-time PCR
    Data Markup Language (RDML) and transforms to the appropriate formats of
    the 'qpcR' and 'chipPCR' packages. Contains a dendrogram visualization 
    for the structure of RDML object and GUI for RDML editing.
	"""
	
	homepage = "https://github.com/kablag/RDML"
	cran = "RDML" 

	version("1.0", md5="89b9f9c9dc36e703df46399b881136f9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-checkmate@1.6.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-piper", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlist@0.4:", type=("build", "run"))
	depends_on("r-r6@2.0.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
