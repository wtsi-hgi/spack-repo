# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsva(RPackage):
	"""Direct Surrogate Variable Analysis

	Functions for direct surrogate variable analysis, which can identify hidden factors in high-dimensional biomedical data.
	"""
	
	cran = "dSVA" 

	version("1.0", md5="56c146e07ec41e3be42a2593e5d40ddb")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
