# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPins(RPackage):
	"""Pin, Discover and Share Resources

	Publish data sets, models, and other R objects, making it
    easy to share them across projects and with your colleagues. You can
    pin objects to a variety of "boards", including local folders (to
    share on a networked drive or with 'DropBox'), 'RStudio' connect,
    Amazon S3, and more.
	"""
	
	homepage = "https://pins.rstudio.com/"
	cran = "pins" 

	version("1.3.0", md5="e14ab2a6c8c1a369c9170a76b82da012")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-withr@2.4.3:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
