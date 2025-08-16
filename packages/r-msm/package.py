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

	# Newer releases needed for R >= 4.5 compatibility
	version("1.8.2", sha256="5b97353978b54d7315bc9690dbfdea0062cc2823d001dbcc035c3420df1ebe26")
	version("1.7.1", sha256="d134782b966eed33742819595119ab1a61bec4416cc3fa7630a0f34c4e7f785b")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	# Additional CRAN dependencies introduced in >=1.8
	depends_on("r-generics", type=("build", "run"), when="@1.8:")
	depends_on("r-tibble", type=("build", "run"), when="@1.8:")
