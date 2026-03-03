# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsub(RPackage):
	"""Running Commands Remotely on 'Gridengine' Clusters

	Run lapply() calls in parallel by submitting them to 
    'gridengine' clusters using the 'qsub' command.
	"""
	
	homepage = "https://github.com/rcannood/qsub"
	cran = "qsub" 

	version("1.1.3", md5="26fa9b5ce67e91db1ef224fa857a5b7c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-random", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-ssh", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
