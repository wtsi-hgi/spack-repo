# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdobeanalyticsr(RPackage):
	"""R Client for 'Adobe Analytics' API 2.0

	Connect to the 'Adobe Analytics' API v2.0 <https://github.com/AdobeDocs/analytics-2.0-apis>
             which powers 'Analysis Workspace'. The package was developed
             with the analyst in mind, and it will continue to be
             developed with the guiding principles of iterative,
             repeatable, timely analysis.
	"""
	
	homepage = "https://github.com/benrwoodard/adobeanalyticsr"
	cran = "adobeanalyticsr" 

	version("0.4.0", md5="fbfc30eda2a4a58d6474bb46dc8672e1")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-httr@1.3.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-rlang@0.4.8:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-jose", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
