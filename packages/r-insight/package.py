# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInsight(RPackage):
	"""Easy Access to Model Information for Various Model Objects.

	A tool to provide an easy, intuitive and consistent access to information
	contained in various R models, like model formulas, model terms,
	information about random effects, data that was used to fit the model or
	data from response variables. 'insight' mainly revolves around two types of
	functions: Functions that find (the names of) information, starting with
	'find_', and functions that get the underlying data, starting with 'get_'.
	The package has a consistent syntax and works with many different model
	objects, where otherwise functions to access these information are
	missing."""

	cran = "insight"

	version("0.19.8", md5="f227772b838f94fd5775fc995c48524d")

	depends_on("r@3.6:", type=("build", "run"))
