# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTibbletime(RPackage):
	"""Time Aware Tibbles

	Built on top of the 'tibble' package, 'tibbletime' is an extension
  that allows for the creation of time aware tibbles. Some immediate
  advantages of this include: the ability to perform time-based subsetting
  on tibbles, quickly summarising and aggregating results by time periods,
  and creating columns that can be used as 'dplyr' time-based groups.
	"""
	
	homepage = "https://github.com/business-science/tibbletime"
	cran = "tibbletime" 

	version("0.1.8", md5="551d4ffd20f8bb670987a4f8367c254d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-hms@1.1.2:", type=("build", "run"))
	depends_on("r-lubridate@1.9.1:", type=("build", "run"))
	depends_on("r-pillar@1.8.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.5:", type=("build", "run"))
	depends_on("r-rcpp@1.0.10:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-vctrs@0.5:", type=("build", "run"))
	depends_on("r-zoo@1.8.11:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
