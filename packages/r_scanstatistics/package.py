# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScanstatistics(RPackage):
	"""Space-Time Anomaly Detection using Scan Statistics

	Detection of anomalous space-time clusters using the scan 
  statistics methodology. Focuses on prospective surveillance of data streams, 
  scanning for clusters with ongoing anomalies. Hypothesis testing is made 
  possible by Monte Carlo simulation. Allévius (2018) <doi:10.21105/joss.00515>.
	"""
	
	homepage = "https://github.com/promerpr/scanstatistics"
	cran = "scanstatistics" 

	version("1.1.1", md5="1b44b8644deef8dc0ff751e19fc9851d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ismev", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
