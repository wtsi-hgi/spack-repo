# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringr(RPackage):
	"""Simple, Consistent Wrappers for Common String Operations.

	A consistent, simple and easy to use set of wrappers around the fantastic
	'stringi' package. All function and argument names (and positions) are
	consistent, all functions deal with "NA"'s and zero length vectors in the
	same way, and the output from one function is easy to feed into the input
	of another."""

	cran = "stringr"

	license("MIT")

	version("1.5.1", md5="75dd96fdaac6520418c92f6c434d3afc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue@1.6.1:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-stringi@1.5.3:", type=("build", "run"))
	depends_on("r-vctrs@0.4:", type=("build", "run"))
