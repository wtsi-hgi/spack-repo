# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabelwhale(RPackage):
	"""Talking to 'Docker' and 'Singularity' Containers

	Provides a unified interface to interact with
    'docker' and 'singularity' containers.  You can execute a command
    inside a container, mount a volume or copy a file.
	"""
	
	homepage = "https://github.com/dynverse/babelwhale"
	cran = "babelwhale" 

	version("1.2.0", md5="1dae15c3e7913f7b905d7b5bcb225fca")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-dynutils", type=("build", "run"))
	depends_on("r-processx@3.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
