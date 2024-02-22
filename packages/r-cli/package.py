# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCli(RPackage):
	"""Helpers for Developing Command Line Interfaces.

	A suite of tools to build attractive command line interfaces ('CLIs'), from
	semantic elements: headings, lists, alerts, paragraphs, etc.  Supports
	custom themes via a 'CSS'-like language. It also contains a number of lower
	level 'CLI' elements: rules, boxes, trees, and 'Unicode' symbols with
	'ASCII' alternatives. It integrates with the 'crayon' package to support
	'ANSI' terminal colors."""

	cran = "cli"

	version("3.6.2", md5="36e2b58e8de26def5fcf17b6dd71dad7")

	depends_on("r@3.4:", type=("build", "run"))
