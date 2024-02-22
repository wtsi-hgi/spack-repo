# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGetoptlong(RPackage):
	"""Parsing Command-Line Arguments and Simple Variable Interpolation.

	This is yet another command-line argument parser which wraps the powerful
	Perl module Getopt::Long and with some adaptation for easier use in R. It
	also provides a simple way for variable interpolation in R."""

	cran = "GetoptLong"

	version("1.0.5", md5="859f5b437ccf1eda9fe0e99eb80b2def")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-globaloptions@0.1:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("perl", type=("build", "link", "run"))
