# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpymat(RPackage):
	"""Easy to Configure an Isolated 'Python' Environment

	Aims to create a single isolated 'Miniconda' 
    and 'Python' environment for reproducible pipeline scripts. 
    The package provides utilities to run system command within the 'conda'
    environment, making it easy to install, launch, manage, and stop 
    'Jupyter-lab'.
	"""
	
	homepage = "https://github.com/dipterix/rpymat"
	cran = "rpymat" 

	version("0.1.7", md5="c7a7d25f4648d47c9b78c6bd5f246a51")

	depends_on("r-reticulate@1.21:", type=("build", "run"))
	depends_on("r-fastmap@1.1:", type=("build", "run"))
	depends_on("r-rappdirs@0.3.3:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-irkernel@1.3:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.3:", type=("build", "run"))
	depends_on("r-rstudioapi@0.13:", type=("build", "run"))
