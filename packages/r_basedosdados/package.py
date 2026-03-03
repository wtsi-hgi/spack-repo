# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasedosdados(RPackage):
	"""'Base Dos Dados' R Client

	An R interface to the 'Base dos Dados' API <https:basedosdados.github.io/mais/py_reference_api/>). Authenticate your project, query our tables, save data to disk and memory, all from R.
	"""
	
	cran = "basedosdados" 

	version("0.2.2", md5="93e9517b3c2acd1ec8e9f295e15bc843")

	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-tibble@3.1.1:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-cli@2.5:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dotenv@1.0.2:", type=("build", "run"))
	depends_on("r-bigrquery@1.4:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-writexl@1.4:", type=("build", "run"))
	depends_on("r-fs@1.5:", type=("build", "run"))
	depends_on("r-dbplyr@2.1.1:", type=("build", "run"))
	depends_on("r-scales@1.1.1:", type=("build", "run"))
	depends_on("r-dbi@1.1.1:", type=("build", "run"))
	depends_on("r-typed@0.0.1:", type=("build", "run"))
