# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiotic(RPackage):
	"""Calculation of Freshwater Biotic Indices

	Calculates a range of UK freshwater invertebrate biotic indices
    including BMWP, Whalley, WHPT, Habitat-specific BMWP, AWIC, LIFE and PSI.
	"""
	
	homepage = "https://github.com/robbriers/biotic"
	cran = "biotic" 

	version("0.1.2", md5="a6ccd76e15e59ef155aaa45fc56a728e")

	depends_on("r@3:", type=("build", "run"))
