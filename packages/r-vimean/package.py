# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVimean(RPackage):
	"""Variability Independent of Mean

	To computed the variability independent of mean (VIM) or variation
    independent of mean (VIM). The methodology can be found at
    Peter M Rothwell et al. (2010) <doi:10.1016/S1474-4422(10)70067-3>.
	"""
	
	cran = "VIMean" 

	version("0.1.0", md5="8448a4d05057a8d4e0b2799e005005be")

