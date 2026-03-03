# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSisal(RPackage):
	"""Sequential Input Selection Algorithm

	Implements the SISAL algorithm by Tikka and Hollmén. It is
        a sequential backward selection algorithm which uses a linear
        model in a cross-validation setting. Starting from the full
        model, one variable at a time is removed based on the
        regression coefficients. From this set of models, a
        parsimonious (sparse) model is found by choosing the model with
        the smallest number of variables among those models where the
        validation error is smaller than a threshold. Also implements
        extensions which explore larger parts of the search space
        and/or use ridge regression instead of ordinary least squares.
	"""
	
	homepage = "https://github.com/mvkorpel/sisal"
	cran = "sisal" 

	version("0.48", md5="3cbff96c54e743d149c42b697bc2dd46")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-r-matlab", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
