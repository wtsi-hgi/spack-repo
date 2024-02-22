# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlumber(RPackage):
	"""An API Generator for R

	Gives the ability to automatically generate and serve an HTTP API
    from R functions using the annotations in the R documentation around your
    functions.
	"""
	
	homepage = "https://www.rplumber.io"
	cran = "plumber" 

	version("1.2.1", md5="e8bcb7780075c4cbc7cd2c2421092029")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-stringi@0.3:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.16:", type=("build", "run"))
	depends_on("r-webutils@1.1:", type=("build", "run"))
	depends_on("r-httpuv@1.5.5:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-promises@1.1:", type=("build", "run"))
	depends_on("r-sodium", type=("build", "run"))
	depends_on("r-swagger@3.33:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-ellipsis@0.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
