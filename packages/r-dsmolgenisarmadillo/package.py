# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsmolgenisarmadillo(RPackage):
	"""'DataSHIELD' Client for 'MOLGENIS Armadillo'

	'DataSHIELD' is an infrastructure and series of R packages that 
    enables the remote and 'non-disclosive' analysis of sensitive research data.
    This package is the 'DataSHIELD' interface implementation to analyze data
    shared on a 'MOLGENIS Armadillo' server. 'MOLGENIS Armadillo' is a
    light-weight 'DataSHIELD' server using a file store and an 'RServe' server.
	"""
	
	homepage = "https://github.com/molgenis/molgenis-r-datashield/"
	cran = "DSMolgenisArmadillo" 

	version("2.0.5", md5="9f466c83f930cd1c2be064f6b572f157")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dsi@1.3:", type=("build", "run"))
	depends_on("r-molgenisauth@0.0.25:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
