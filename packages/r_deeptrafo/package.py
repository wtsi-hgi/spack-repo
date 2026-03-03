# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeeptrafo(RPackage):
	"""Fitting Deep Conditional Transformation Models

	Allows for the specification of deep conditional transformation 
    models (DCTMs) and ordinal neural network transformation models, as 
    described in Baumann et al (2021) <doi:10.1007/978-3-030-86523-8_1> and 
    Kook et al (2022) <doi:10.1016/j.patcog.2021.108263>. Extensions such as
    autoregressive DCTMs (Ruegamer et al, 2022, <doi:10.48550/arXiv.2110.08248>)
    and transformation ensembles (Kook et al, 2022, <doi:10.48550/arXiv.2205.12729>)
    are implemented.
	"""
	
	cran = "deeptrafo" 

	version("0.1-1", md5="2b2066055348c3a4de71ab432a1a114b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-keras@2.2:", type=("build", "run"))
	depends_on("r-tfprobability@0.15:", type=("build", "run"))
	depends_on("r-deepregression", type=("build", "run"))
	depends_on("r-mlt", type=("build", "run"))
	depends_on("r-variables", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
