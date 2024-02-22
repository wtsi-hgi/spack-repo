# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbrace(RPackage):
	"""Curly Braces for 'ggplot2'

	Provides curly braces in 'ggplot2' plus matching text.
    stat_brace() plots braces partially in the confines of data so that the brace is set apart from it.
    stat_bracetext() plots corresponding text, fitting to the braces from stat_brace().
	"""
	
	cran = "ggbrace" 

	version("0.1.1", md5="2b3537c91c545bd92bb01483827c5aee")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.2:", type=("build", "run"))
