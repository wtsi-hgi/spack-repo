# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RF1datar(RPackage):
	"""Access Formula 1 Data

	Obtain Formula 1 data via the 'Ergast API' <https://ergast.com/mrd/> and the unofficial API <https://www.formula1.com/en/f1-live.html> via the 'fastf1' 'Python' library <https://docs.fastf1.dev/>.
	"""
	
	homepage = "https://scasanova.github.io/f1dataR/"
	cran = "f1dataR" 

	version("1.5.0", md5="78e566071dc11a76d998d43d9860135b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-reticulate@1.14:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
