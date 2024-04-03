# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopbio(RPackage):
	"""Construction and Analysis of Matrix Population Models

	Construct and analyze projection matrix models from a demography study of marked individuals classified by age or stage. The package covers methods described in Matrix Population Models by Caswell (2001) and Quantitative Conservation Biology by Morris and Doak (2002).
	"""
	
	cran = "popbio" 

	version("2.8", md5="e485e70631dbf52b20118daa180908a0")

