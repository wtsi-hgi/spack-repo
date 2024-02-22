# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYmlthis(RPackage):
	"""Write 'YAML' for 'R Markdown', 'bookdown', 'blogdown', and More

	Write 'YAML' front matter for R Markdown and related
    documents. Work with 'YAML' objects more naturally and write the
    resulting 'YAML' to your clipboard or to 'YAML' files related to your
    project.
	"""
	
	homepage = "https://ymlthis.r-lib.org"
	cran = "ymlthis" 

	version("0.1.7", md5="adef5b9688045a0816b18b189fbb0ddd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-rmarkdown@2.10:", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-usethis@1.5:", type=("build", "run"))
	depends_on("r-whoami", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
