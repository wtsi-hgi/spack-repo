# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFtextra(RPackage):
	"""Extensions for 'Flextable'

	Build display tables easily by extending the functionality of the
    'flextable' package. Features include spanning header, grouping rows,
    parsing markdown and so on.
	"""
	
	homepage = "https://ftextra.atusy.net"
	cran = "ftExtra" 

	version("0.6.2", md5="63bd1b28ee9b6230407b1cfecfc2a7a1")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-flextable@0.8.3:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect@1.1:", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("pandoc@2.0.6:", type=("build", "link", "run"))
