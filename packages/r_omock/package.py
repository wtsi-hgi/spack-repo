# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmock(RPackage):
	"""Creation of Mock Observational Medical Outcomes Partnership
Common Data Model

	Creates mock data for testing and package development for the
    Observational Medical Outcomes Partnership common data model. The
    package offers functions crafted with pipeline-friendly
    implementation, enabling users to effortlessly include only the
    necessary tables for their testing needs.
	"""
	
	homepage = "https://oxford-pharmacoepi.github.io/omock/"
	cran = "omock" 

	version("0.1.0", md5="70ac29ecfcb8fdf8db299f57d234b2a8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-omopgenerics@0.0.3:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snakecase", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
