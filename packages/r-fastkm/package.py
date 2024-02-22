# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastkm(RPackage):
	"""A Fast Multiple-Kernel Method Based on a Low-Rank Approximation

	A computationally efficient and statistically rigorous fast 
    Kernel Machine method for multi-kernel analysis. The approach is based on 
    a low-rank approximation to the nuisance effect kernel matrices. The 
    algorithm is applicable to continuous, binary, and survival traits and 
    is implemented using the existing single-kernel analysis software 'SKAT' 
    and 'coxKM'. 'coxKM' can be obtained from 
    <https://github.com/lin-lab/coxKM>.
	"""
	
	cran = "FastKM" 

	version("1.1", md5="7f8b1a88005dcf8c2ee3d8ccb3a08ad6")

	depends_on("r-rarpack", type=("build", "run"))
