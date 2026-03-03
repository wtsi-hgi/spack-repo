# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrmn(RPackage):
	"""CCMN and Other Normalization Methods for Metabolomics Data

	Implements the Cross-contribution Compensating Multiple
    standard Normalization (CCMN) method described in Redestig et
    al. (2009) Analytical Chemistry <doi:10.1021/ac901143w>
    and other normalization algorithms.
	"""
	
	homepage = "https://github.com/hredestig/crmn"
	cran = "crmn" 

	version("0.0.21", md5="6fad89001340c1f5702be101f971769e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pcamethods@1.56:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
