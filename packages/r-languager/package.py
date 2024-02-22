# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLanguager(RPackage):
	"""Analyzing Linguistic Data: A Practical Introduction to
Statistics

	Data sets exemplifying statistical methods, and some
        facilitatory utility functions used in ``Analyzing Linguistic
        Data: A practical introduction to statistics using R'',
        Cambridge University Press, 2008.
	"""
	
	cran = "languageR" 

	version("1.5.0", md5="80b2d922c5adc1950e70a4c2693b1738")

	depends_on("r@3.0.2:", type=("build", "run"))
