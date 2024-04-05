# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPointblank(RPackage):
	"""Data Validation and Organization of Metadata for Local and
Remote Tables

	Validate data in data frames, 'tibble' objects, 'Spark'
    'DataFrames', and database tables. Validation pipelines can be made using
    easily-readable, consecutive validation steps. Upon execution of the
    validation plan, several reporting options are available. User-defined
    thresholds for failure rates allow for the determination of appropriate
    reporting actions. Many other workflows are available including an
    information management workflow, where the aim is to record, collect, and
    generate useful information on data tables.
	"""
	
	homepage = "https://rstudio.github.io/pointblank/"
	cran = "pointblank" 

	version("0.12.1", md5="d24d6ef7fe4914ecc6cc8ba3832f6c5c")
	version("0.11.4", md5="fc3341e05a396524c75eb03be120f25e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-base64enc@0.1.3:", type=("build", "run"))
	depends_on("r-blastula@0.3.3:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-digest@0.6.27:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-dbplyr@2.3:", type=("build", "run"))
	depends_on("r-fs@1.6:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-gt@0.9:", type=("build", "run"))
	depends_on("r-htmltools@0.5.4:", type=("build", "run"))
	depends_on("r-knitr@1.42:", type=("build", "run"))
	depends_on("r-rlang@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-scales@1.2.1:", type=("build", "run"))
	depends_on("r-testthat@3.1.6:", type=("build", "run"))
	depends_on("r-tibble@3.1.8:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-yaml@2.3.7:", type=("build", "run"))
