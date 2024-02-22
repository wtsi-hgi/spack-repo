# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRccpca(RPackage):
	""""Retained Component Criterion for Principal Component Analysis"

	The RCC_PCA criterion is a tool to determine the optimal number of components to retain in PCA;See Alshammri (2021).
	"""
	
	cran = "RCCPCA" 

	version("0.1.0", md5="897fea6b6f8adb18a221001cfebb6d22")

