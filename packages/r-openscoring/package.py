# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenscoring(RPackage):
	"""'Open Scoring' API Client

	Creativity research involves the need to score open-ended problems.
  Usually done by humans, automatic scoring using AI becomes more
  and more accurate. This package provides a simple interface to
  the 'Open Scoring' API <https://openscoring.du.edu/docs>, leading creativity scoring technology by
  Organiscak et al. (2023) <doi:10.1016/j.tsc.2023.101356>. With it,
  you can score your own data directly from an R script.
	"""
	
	homepage = "https://github.com/jakub-jedrusiak/openscoring"
	cran = "openscoring" 

	version("1.0.1", md5="2dd4fe160bfd67c9d04b8585d1900a39")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
