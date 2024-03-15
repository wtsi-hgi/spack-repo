# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHardhat(RPackage):
	"""Construct Modeling Packages.

	Building modeling packages is hard. A large amount of effort generally goes
	into providing an implementation for a new method that is efficient, fast,
	and correct, but often less emphasis is put on the user interface. A good
	interface requires specialized knowledge about S3 methods and formulas,
	which the average package developer might not have. The goal of 'hardhat'
	is to reduce the burden around building new modeling packages by providing
	functionality for preprocessing, predicting, and validating input."""

	cran = "hardhat"

	license("MIT")

	version("1.3.1", md5="0b0462377860197342dcb16311355a1a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-vctrs@0.6:", type=("build", "run"))
