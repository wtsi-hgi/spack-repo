# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResponsepatterns(RPackage):
	"""Screening for Careless Responding Patterns

	Some survey participants tend to respond carelessly which complicates data analysis. This package provides functions that make it easier to explore responses and identify those that may be problematic. See Gottfried et al. (2022) <doi:10.7275/vyxb-gt24> for more information.
	"""
	
	cran = "responsePatterns" 

	version("0.1.1", md5="28169bc71c7f470fc488cabe4f3ee834")

	depends_on("r@3.5:", type=("build", "run"))
