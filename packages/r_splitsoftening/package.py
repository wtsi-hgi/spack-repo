# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplitsoftening(RPackage):
	"""Softening Splits in Decision Trees

	Allows to produce and use classification trees with soft (probability) splits,
	as described in: Dvořák, J. (2019), <doi:10.1007/s00180-019-00867-1>.
	"""
	
	cran = "SplitSoftening" 

	version("2.1-0", md5="7b4a661e25acf7c4b92d68140cf87c19")

	depends_on("r@3:", type=("build", "run"))
