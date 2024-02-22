# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParade(RPackage):
	"""Pen's Income Parades

	Tool for producing Pen's parade graphs, useful for visualizing inequalities in income, wages or other variables, as proposed by Pen (1971, ISBN: 978-0140212594). Income or another economic variable is captured by the vertical axis, while the population is arranged in ascending order of income along the horizontal axis. Pen's income parades provide an easy-to-interpret visualization of economic inequalities.
	"""
	
	cran = "parade" 

	version("0.1", md5="7538b8aa2821e650f57f53a2783adf6b")

