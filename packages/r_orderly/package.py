# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrderly(RPackage):
	"""Lightweight Reproducible Reporting

	Order, create and store reports from R.  By defining a
    lightweight interface around the inputs and outputs of an
    analysis, a lot of the repetitive work for reproducible research
    can be automated.  We define a simple format for organising and
    describing work that facilitates collaborative reproducible
    research and acknowledges that all analyses are run multiple
    times over their lifespans.
	"""
	
	homepage = "https://www.vaccineimpact.org/orderly/"
	cran = "orderly" 

	version("1.4.3", md5="2813e115ee1ef9229c04fc5fe760b1c2")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rsqlite@2.2.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-docopt", type=("build", "run"))
	depends_on("r-fs@1.2.7:", type=("build", "run"))
	depends_on("r-gert", type=("build", "run"))
	depends_on("r-ids", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-zip@2:", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
