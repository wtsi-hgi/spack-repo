# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlume(RPackage):
	"""A Simple Author Handler for Scientific Writing

	Handles and formats author information in scientific writing
    in 'R Markdown' and 'Quarto'. 'plume' provides easy-to-use and
    flexible tools for injecting author metadata in 'YAML' headers as well
    as generating author and contribution lists (among others) as strings
    from tabular data.
	"""
	
	homepage = "https://arnaudgallou.github.io/plume/"
	cran = "plume" 

	version("0.2.3", md5="b10c398659c0bb9891a634229182cd81")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-glue@1.3.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-knitr@1.40:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-tidyr@1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-yaml@2.3.5:", type=("build", "run"))
