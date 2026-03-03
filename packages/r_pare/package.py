# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPare(RPackage):
	"""A Way to Perform Code Review or QA on Other Packages

	Reviews other packages during code review by looking at their
    dependencies, code style, code complexity, and how internally defined
    functions interact with one another.
	"""
	
	homepage = "https://github.com/darwin-eu-dev/PaRe"
	cran = "PaRe" 

	version("0.1.12", md5="473f93e8d4866d1b06ba804efb75429d")

	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-cyclocomp@1.1:", type=("build", "run"))
	depends_on("r-desc@1.4.2:", type=("build", "run"))
	depends_on("r-diagrammer@1.0.9:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-lintr@3.0.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-pak@0.2:", type=("build", "run"))
	depends_on("r-rmarkdown@2.20:", type=("build", "run"))
	depends_on("r-rsvg@2.4:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-igraph@1.3.5:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-git2r@0.31:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
