# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyselect(RPackage):
	"""Select from a Set of Strings.

	A backend for the selecting functions of the 'tidyverse'. It makes it easy
	to implement select-like functions in your own packages in a way that is
	consistent with other 'tidyverse' interfaces for selection."""

	cran = "tidyselect"

	license("MIT")

	version("1.2.1", md5="49c581292e819a2a39aac321f27ab0a8")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.0.4:", type=("build", "run"))
	depends_on("r-vctrs@0.5.2:", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
