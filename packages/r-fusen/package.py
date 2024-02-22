# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFusen(RPackage):
	"""Build a Package from Rmarkdown Files

	Use Rmarkdown First method to build your package. Start your
    package with documentation, functions, examples and tests in the same
    unique file. Everything can be set from the Rmarkdown template file
    provided in your project, then inflated as a package. Inflating the
    template copies the relevant chunks and sections in the appropriate
    files required for package development.
	"""
	
	homepage = "https://thinkr-open.github.io/fusen/"
	cran = "fusen" 

	version("0.5.2", md5="dedad77d7ea45b3b0b177c069ae072bd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-attachment", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-here@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-parsermd@0.1:", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-usethis@2:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
