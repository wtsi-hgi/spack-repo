# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlabkey(RPackage):
	"""Data Exchange Between R and 'LabKey' Server

	The 'LabKey' client library for R makes it easy for R users to
    load live data from a 'LabKey' Server, <https://www.labkey.com/>,
    into the R environment for analysis, provided users have permissions
    to read the data. It also enables R users to insert, update, and
    delete records stored on a 'LabKey' Server, provided they have appropriate
    permissions to do so.
	"""
	
	cran = "Rlabkey" 

	version("3.2.0", md5="3ac1bc144d1dabd25d8b8d7fba249c7f")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
