# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpfilter(RPackage):
	"""The One- And Two-Sided Hodrick-Prescott Filter

	Provides two functions that implement the one-sided and
    two-sided versions of the Hodrick-Prescott filter. The one-sided
    version is a Kalman filter-based implementation, whereas the two-
    sided version uses sparse matrices for improved efficiency.
    References:
    Hodrick, R. J., and Prescott, E. C. (1997) <doi:10.2307/2953682>
    Mcelroy, T. (2008) <doi:10.1111/j.1368-423X.2008.00230.x>
    Meyer-Gohde, A. (2010) <https://ideas.repec.org/c/dge/qmrbcd/181.html>
    For more references, see the vignette.
	"""
	
	homepage = "https://www.alexandrumonahov.eu.org/projects"
	cran = "hpfilter" 

	version("1.0.2", md5="41fa4af6c13539b8fc92ceca536c2e25")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
