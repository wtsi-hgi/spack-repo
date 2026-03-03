# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiPluginDeoptim(RPackage):
	"""'DEoptim' and 'DEoptimR' Plugin for the 'R' Optimization
Interface

	Enhances the R Optimization Infrastructure ('ROI') package
        	 with the 'DEoptim' and 'DEoptimR' package. 'DEoptim' is
        	 used for unconstrained optimization and 'DEoptimR' for
        	 constrained optimization.
	"""
	
	homepage = "https://roigrp.gitlab.io"
	cran = "ROI.plugin.deoptim" 

	version("1.0-2", md5="94ce8a41be32d89172509b26172ca563")

	depends_on("r-roi@1.0.0:", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-deoptimr@1.0.10:", type=("build", "run"))
