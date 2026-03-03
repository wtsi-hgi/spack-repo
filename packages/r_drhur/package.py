# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrhur(RPackage):
	"""Learning R with Dr. Hu

	Tutarials of R learning easily and happily.
	"""
	
	cran = "drhur" 

	version("1.1.0", md5="003616b540479bd91ec28ff43cc0246b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-learnr@0.10.1:", type=("build", "run"))
