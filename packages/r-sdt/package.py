# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdt(RPackage):
	"""Self-Determination Theory Measures

	Functions for self-determination motivation theory (SDT) to compute
    measures of motivation internalization, motivation simplex structure, and of
    the original and adjusted self-determination or relative autonomy index. SDT
    was introduced by Deci and Ryan (1985) <doi:10.1007/978-1-4899-2271-7>. See
    package?SDT for an overview.
	"""
	
	homepage = "http://www.meb.edu.tum.de"
	cran = "SDT" 

	version("1.0.0", md5="63e4535079483e65a9e78ee25e420fda")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
