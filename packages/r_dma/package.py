# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDma(RPackage):
	"""Dynamic Model Averaging

	Dynamic model averaging for binary and continuous
        outcomes.
	"""
	
	cran = "dma" 

	version("1.4-0", md5="c9445cd7ac28be2cee36e3778c7e5179")

	depends_on("r-mass", type=("build", "run"))
