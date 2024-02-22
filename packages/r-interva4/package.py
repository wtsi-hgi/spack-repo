# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInterva4(RPackage):
	"""Replicate and Analyse 'InterVA4'

	Provides an R version of the 'InterVA4' software (<http://www.interva.net>) for coding cause of death from verbal autopsies. It also provides simple graphical representation of individual and population level statistics.
	"""
	
	cran = "InterVA4" 

	version("1.7.6", md5="22d90d747e28e12beca450e6ea07bd85", url="https://cran.r-project.org/src/contrib/InterVA4_1.7.6.tar.gz")

