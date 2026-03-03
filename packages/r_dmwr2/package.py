# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmwr2(RPackage):
	"""Functions and Data for the Second Edition of "Data Mining with
R"

	Functions and data accompanying the second edition of the book  "Data Mining with R, learning with case studies" by Luis Torgo, published by CRC Press.
	"""
	
	homepage = "https://github.com/ltorgo/DMwR2"
	cran = "DMwR2" 

	version("0.0.2", md5="90be151675987b0ad90531e77d48066f", url="https://cran.r-project.org/src/contrib/DMwR2_0.0.2.tar.gz")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-xts@0.9.7:", type=("build", "run"))
	depends_on("r-zoo@1.7.10:", type=("build", "run"))
	depends_on("r-class@7.3.14:", type=("build", "run"))
	depends_on("r-rpart@4.1.10:", type=("build", "run"))
	depends_on("r-quantmod@0.4.5:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
	depends_on("r-dbi@0.5:", type=("build", "run"))
