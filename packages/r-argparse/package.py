# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArgparse(RPackage):
	"""Command Line Optional and Positional Argument Parser.

	A command line parser to be used with Rscript to write "#!" shebang scripts
	that gracefully accept positional and optional arguments and automatically
	generate usage."""

	cran = "argparse"

	version("2.2.2", md5="fe22b79b423ac686d072694fe30b8617")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-findpython", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("python@3.2:", type=("build", "link", "run"))
