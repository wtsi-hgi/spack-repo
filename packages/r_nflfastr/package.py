# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNflfastr(RPackage):
	"""Functions to Efficiently Access NFL Play by Play Data

	A set of functions to access National Football
    League play-by-play data from <https://www.nfl.com/>.
	"""
	
	homepage = "https://www.nflfastr.com/"
	cran = "nflfastR" 

	version("4.6.1", md5="6e8e20b1a666440f822572d10665893a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fastrmodels@1.0.1:", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-nflreadr@1.2:", type=("build", "run"))
	depends_on("r-progressr@0.6:", type=("build", "run"))
	depends_on("r-rlang@0.4.7:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-xgboost@1.1:", type=("build", "run"))
