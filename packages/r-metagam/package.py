# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagam(RPackage):
	"""Meta-Analysis of Generalized Additive Models

	Meta-analysis of generalized additive
    models and generalized additive mixed models. A typical use case is
    when data cannot be shared across locations, and an overall meta-analytic
    fit is sought. 'metagam' provides functionality for removing individual
    participant data from models computed using the 'mgcv' and 'gamm4' packages such
    that the model objects can be shared without exposing individual data.
    Furthermore, methods for meta-analysing these fits are provided. The implemented
    methods are described in Sorensen et al. (2020), <doi:10.1016/j.neuroimage.2020.117416>,
    extending previous works by Schwartz and Zanobetti (2000)
    and Crippa et al. (2018) <doi:10.6000/1929-6029.2018.07.02.1>.
	"""
	
	homepage = "https://lifebrain.github.io/metagam/"
	cran = "metagam" 

	version("0.4.0", md5="0c197dcc66f5a602dbed6f3de3874990")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
