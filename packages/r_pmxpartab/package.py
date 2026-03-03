# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmxpartab(RPackage):
	"""Parameter Tables for PMx Analyses

	Generate nicely formatted HTML tables to display estimation results for
  pharmacometric models.
	"""
	
	cran = "pmxpartab" 

	version("0.5.0", md5="012c032a34cd9ec3af682d9540a79eb6")

	depends_on("r-table1", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
