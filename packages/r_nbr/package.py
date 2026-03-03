# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNbr(RPackage):
	"""Network-Based R-Statistics using Mixed Effects Models

	An implementation of network-based statistics in R using mixed effects models.
    Theoretical background for Network-Based Statistics can be found in Zalesky et al. (2010)
    <doi:10.1016/j.neuroimage.2010.06.041>. For Mixed Effects Models check the
    R package <https://CRAN.R-project.org/package=nlme>.
	"""
	
	cran = "NBR" 

	version("0.1.5", md5="ea2f11c2a2a46f08e75f3f04e46d4af0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
