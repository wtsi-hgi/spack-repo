# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeuroblastoma(RPackage):
	"""Neuroblastoma Copy Number Profiles

	
 Annotated neuroblastoma copy number profiles,
 a benchmark data set for change-point detection algorithms,
 as described by Hocking et al. <doi:10.1186/1471-2105-14-164>.
	"""
	
	cran = "neuroblastoma" 

	version("2023.9.3", md5="fb7ce5aa0b98c15b645ddda3ef790500")

	depends_on("r@3.5:", type=("build", "run"))
