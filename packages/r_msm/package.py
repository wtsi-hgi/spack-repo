# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsm(RPackage):
	"""Multi-State Markov and Hidden Markov Models in Continuous Time

	Functions for fitting continuous-time Markov and hidden
    Markov multi-state models to longitudinal data.  Designed for
    processes observed at arbitrary times in continuous time (panel data)
    but some other observation schemes are supported. Both Markov
    transition rates and the hidden Markov output process can be modelled
    in terms of covariates, which may be constant or piecewise-constant
    in time.
	"""
	
	homepage = "https://github.com/chjackson/msm"
	cran = "msm" 

	version("1.7.1", md5="8aa592740ac775876b23cb0eb28b36d6")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
