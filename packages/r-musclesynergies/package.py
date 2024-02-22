# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMusclesynergies(RPackage):
	"""Extract Muscle Synergies from Electromyography

	Provides a framework to factorise electromyography (EMG) data.
    Tools are provided for raw data pre-processing, non negative matrix factorisation,
    classification of factorised data and plotting of obtained outcomes.
    In particular, reading from ASCII files is supported, along with wide-used
    filtering approaches to process EMG data. All steps include one or more sensible
    defaults that aim at simplifying the workflow. Yet, all functions are largely
    tunable at need. Example data sets are included.
	"""
	
	homepage = "https://github.com/alesantuz/musclesyneRgies"
	cran = "musclesyneRgies" 

	version("1.2.5", md5="52af3a815c3578eeca25b7623ed7de0c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-umap", type=("build", "run"))
