# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRematch(RPackage):
	"""Match Regular Expressions with a Nicer 'API'.

	A small wrapper on 'regexpr' to extract the matches and captured groups
	from the match of a regular expression to a character vector."""

	cran = "rematch"

	version("2.0.0", md5="64ad138fd1cec37d50683cbf2958e47b")

