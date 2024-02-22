# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsf(RPackage):
	"""Report of Statistical Findings in 'bookdown'

	A report of statistical findings (RSF) project template is
    generated using a 'bookdown' format. 'YAML' fields can be further
    customized. Additional helper functions provide extra features to the
    RSF.
	"""
	
	homepage = "https://github.com/dchiu911/rsf/"
	cran = "rsf" 

	version("0.3.0", md5="4e955812737e2b1ab03dcedd839c16dd")

	depends_on("r-bookdown", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-renv", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-ymlthis", type=("build", "run"))
