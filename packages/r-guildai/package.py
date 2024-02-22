# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGuildai(RPackage):
	"""Track Machine Learning Experiments

	'Guild AI' is an open-source tool for managing machine learning
    experiments. It's for scientists, engineers, and researchers who want to
    run scripts, compare results, measure progress, and automate machine
    learning workflow. 'Guild AI' is a light weight, external tool that runs
    locally. It works with any framework, doesn't require any changes to
    your code, or access to any web services. Users can easily record
    experiment metadata, track model changes, manage experiment artifacts,
    tune hyperparameters, and share results. 'Guild AI' combines features
    from 'Git', 'SQLite', and 'Make' to provide a lab notebook for machine
    learning.
	"""
	
	homepage = "https://guildai.github.io/guildai-r/"
	cran = "guildai" 

	version("0.0.1", md5="9180e8a3ddbb08d2e250a2984c0f73f4")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-config", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
