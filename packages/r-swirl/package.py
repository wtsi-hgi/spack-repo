# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwirl(RPackage):
	"""Learn R, in R

	Use the R console as an interactive learning
    environment. Users receive immediate feedback as they are guided through
    self-paced lessons in data science and R programming.
	"""
	
	homepage = "http://swirlstats.com"
	cran = "swirl" 

	version("2.4.5", md5="db9247bb3fcb1206db029da5a118f751")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testthat@1.0.2:", type=("build", "run"))
	depends_on("r-httr@1.1:", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
