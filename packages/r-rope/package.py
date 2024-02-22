# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRope(RPackage):
	"""Model Selection with FDR Control of Selected Variables

	Selects one model with variable selection FDR controlled at a
    specified level. A q-value for each potential variable is also returned. The
    input, variable selection counts over many bootstraps for several levels of
    penalization, is modeled as coming from a beta-binomial mixture
    distribution.
	"""
	
	cran = "rope" 

	version("1.0", md5="6776890ca79ed027486255b5cff17ba4")

	depends_on("r@3.1:", type=("build", "run"))
