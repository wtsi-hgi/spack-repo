# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoghorn(RPackage):
	"""Summarize CRAN Check Results in the Terminal

	The CRAN check results and where your package stands in the
    CRAN submission queue in your R terminal.
	"""
	
	homepage = "https://fmichonneau.github.io/foghorn/"
	cran = "foghorn" 

	version("1.5.2", md5="af7785e6a9cfcdfd9ac0b6de0727bcde")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-clisymbols@1:", type=("build", "run"))
	depends_on("r-crayon@1.3.2:", type=("build", "run"))
	depends_on("r-curl@2.2:", type=("build", "run"))
	depends_on("r-httr2@0.2.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.3:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-xml2@1:", type=("build", "run"))
