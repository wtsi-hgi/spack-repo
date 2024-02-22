# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVitality(RPackage):
	"""Fitting Routines for the Vitality Family of Mortality Models

	Provides fitting routines for four versions of the
        Vitality family of mortality models.
	"""
	
	cran = "vitality" 

	version("1.3", md5="a4407bfa15c3ef6993840a15b69e5939")

