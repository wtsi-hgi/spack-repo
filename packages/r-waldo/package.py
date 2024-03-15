# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaldo(RPackage):
	"""Find Differences Between R Objects.

	Compare complex R objects and reveal the key differences. Designed
	particularly for use in testing packages where being able to quickly
	isolate key differences makes understanding test failures much easier."""

	cran = "waldo"

	license("MIT")

	version("0.5.2", md5="51dbfeb0bcc974efcdd7f3d636043984")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-diffobj@0.3.4:", type=("build", "run"))
	depends_on("r-fansi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rematch2", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
