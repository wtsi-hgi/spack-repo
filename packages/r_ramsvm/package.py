# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamsvm(RPackage):
	"""Reinforced Angle-Based Multicategory Support Vector Machines

	Provides a solution path for Reinforced Angle-based Multicategory 
    Support Vector Machines, with linear learning, polynomial learning, and 
    Gaussian kernel learning. C. Zhang, Y. Liu, J. Wang and H. Zhu. (2016) 
    <doi:10.1080/10618600.2015.1043010>.
	"""
	
	cran = "ramsvm" 

	version("2.3", md5="c47a9d32a9b32b563afe5caf33fa5d03")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
