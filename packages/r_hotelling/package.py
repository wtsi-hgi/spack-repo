# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHotelling(RPackage):
	"""Hotelling's T^2 Test and Variants

	A set of R functions which implements Hotelling's T^2 test and some variants of it. Functions are also included for Aitchison's additive log ratio and centred log ratio transformations.
	"""
	
	homepage = "https://github.com/jmcurran/Hotelling"
	cran = "Hotelling" 

	version("1.0-8", md5="976c541f321b952ada0158fcc59a4c88")

	depends_on("r-corpcor", type=("build", "run"))
