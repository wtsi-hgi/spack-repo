# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptparse(RPackage):
	"""Command Line Option Parser.

	A command line parser inspired by Python's 'optparse' library to be used
	with Rscript to write "#!" shebang scripts that accept short and long
	flag/options"""

	cran = "optparse"

	version("1.7.4", md5="f47ae53b0e8096cc86de608d868fb303")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-getopt@1.20.2:", type=("build", "run"))
