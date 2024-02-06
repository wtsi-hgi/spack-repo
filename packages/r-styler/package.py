# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStyler(RPackage):
	"""Non-Invasive Pretty Printing of R Code.

	Pretty-prints R code without changing the user's formatting intent."""

	cran = "styler"

	version("1.10.2", md5="16b84cbb730f29650a8a6f930effc726")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3.1.1:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
	depends_on("r-r-cache@0.15:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-rprojroot@1.1:", type=("build", "run"))
	depends_on("r-vctrs@0.4.1:", type=("build", "run"))
	depends_on("r-withr@2.3:", type=("build", "run"))
