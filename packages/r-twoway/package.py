# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwoway(RPackage):
	"""Analysis of Two-Way Tables

	Carries out analyses of two-way tables with one observation per cell, together with graphical displays
    for an additive fit and
    a diagnostic plot for removable 'non-additivity' via a power transformation of the response.
    It implements Tukey's Exploratory Data Analysis (1973) <ISBN: 978-0201076165> methods, including a
    1-degree-of-freedom test for row*column 'non-additivity', linear in the row and column effects.
	"""
	
	homepage = "https://github.com/friendly/twoway"
	cran = "twoway" 

	version("0.6.3", md5="f6d57963f6d263e43285a05bc0bf274e")

