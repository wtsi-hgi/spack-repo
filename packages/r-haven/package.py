# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHaven(RPackage):
	"""Import and Export 'SPSS', 'Stata' and 'SAS' Files.

	Import foreign statistical formats into R via the embedded 'ReadStat' C
	library, <https://github.com/WizardMac/ReadStat>."""

	cran = "haven"

	license("MIT")

	version("2.5.4", md5="ef0337da48b61ae98b03413e02177822")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli@3:", type=("build", "run"))
	depends_on("r-forcats@0.2:", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-readr@0.1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
