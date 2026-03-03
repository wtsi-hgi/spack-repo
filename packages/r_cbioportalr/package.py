# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbioportalr(RPackage):
	"""Browse and Query Clinical and Genomic Data from cBioPortal

	Provides R users with direct access to genomic and clinical data from the 'cBioPortal' web resource via user-friendly
    functions that wrap 'cBioPortal's' existing API endpoints <https://www.cbioportal.org/api/swagger-ui/index.html>. Users can browse and query genomic data on mutations,
    copy number alterations and fusions, as well as data on tumor mutational burden ('TMB'),
    microsatellite instability status ('MSI'), 'FACETS' and select clinical data points (depending on the study). 
    See <https://www.cbioportal.org/> and Gao et al., (2013) <doi:10.1126/scisignal.2004088> for more information on the cBioPortal web resource.
	"""
	
	homepage = "https://github.com/karissawhiting/cbioportalR"
	cran = "cbioportalR" 

	version("1.1.0", md5="e1dd636e65898603949e61d9dde35edd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr@1.4.3:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.0.3:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
