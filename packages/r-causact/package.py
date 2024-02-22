# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausact(RPackage):
	"""Fast, Easy, and Visual Bayesian Inference

	Accelerate Bayesian analytics workflows in 'R' through interactive modelling,
    visualization, and inference. Define probabilistic graphical models using directed
    acyclic graphs (DAGs) as a unifying language for business stakeholders, statisticians, 
    and programmers. This package relies on interfacing with the 'numpyro' python package. 
	"""
	
	homepage = "https://github.com/flyaflya/causact"
	cran = "causact" 

	version("0.5.3", md5="d99a23be82d787331f8a9bd6d31e7048")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-diagrammer@1.0.9:", type=("build", "run"))
	depends_on("r-dplyr@1.0.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-rlang@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-igraph@1.2.7:", type=("build", "run"))
	depends_on("r-stringr@1.4.1:", type=("build", "run"))
	depends_on("r-cowplot@1.1:", type=("build", "run"))
	depends_on("r-forcats@0.5:", type=("build", "run"))
	depends_on("r-rstudioapi@0.11:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.2:", type=("build", "run"))
	depends_on("r-reticulate@1.30:", type=("build", "run"))
	depends_on("python@3.8:", type=("build", "link", "run"))
