# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBracer(RPackage):
	"""Brace Expansions

	Performs brace expansions on strings.  Made popular by Unix shells, brace expansion allows users to concisely generate certain character vectors by taking a single string and (recursively) expanding the comma-separated lists and double-period-separated integer and character sequences enclosed within braces in that string.  The double-period-separated numeric integer expansion also supports padding the resulting numbers with zeros.
	"""
	
	homepage = "https://trevorldavis.com/R/bracer/"
	cran = "bracer" 

	version("1.2.2", md5="f3772fe59be1602c3f6bdd0188b70f21")

	depends_on("r-stringr", type=("build", "run"))
