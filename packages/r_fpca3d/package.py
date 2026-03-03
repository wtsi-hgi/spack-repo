# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpca3d(RPackage):
	"""Three Dimensional Functional Component Analysis

	Run three dimensional functional principal component analysis and return the three dimensional functional principal component scores. The details of the method are explained in Lin et al.(2015) <doi:10.1371/journal.pone.0132945>.
	"""
	
	cran = "FPCA3D" 

	version("1.0", md5="896bc6a62b9c13541fe40af526a6e8bc")

