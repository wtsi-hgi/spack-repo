# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetopt(RPackage):
	"""C-Like 'getopt' Behavior.

	Package designed to be used with Rscript to write "#!" shebang scripts that
	accept short and long flags/options. Many users will prefer using instead
	the packages optparse or argparse which add extra features like
	automatically generated help option and usage, support for default values,
	positional argument support, etc."""

	cran = "getopt"

	version("1.20.4", md5="78783a3b9aa4c05177b71cf992ff89c6")

