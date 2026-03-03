# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesignsize(RPackage):
	"""Sample Size Calculation of Various Study Designs

	Different sample size calculations with different study designs.
             These techniques are explained by Chow (2007)
             <doi:10.1201/9781584889830>.
	"""
	
	cran = "designsize" 

	version("0.1.0", md5="dd6cc76e26d67b7881ef4431bbe4cc63")

	depends_on("r@3.5:", type=("build", "run"))
