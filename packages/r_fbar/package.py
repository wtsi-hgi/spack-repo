# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbar(RPackage):
	"""An Extensible Approach to Flux Balance Analysis

	A toolkit for Flux Balance Analysis and related
    metabolic modeling techniques. Functions are provided for: parsing
    models in tabular format, converting parsed metabolic models to input
    formats for common linear programming solvers, and
    evaluating and applying gene-protein-reaction mappings. In addition, there
    are wrappers to parse a model, select a solver, find the metabolic fluxes,
    and return the results applied to the original model. Compared to other
    packages in this field, this package puts a much heavier focus on
    providing reusable components that can be used in the design of new
    implementation of new techniques, in particular those that involve large
    parameter sweeps. For a background on the theory, see What is Flux Balance 
    Analysis <doi:10.1038/nbt.1614>.
	"""
	
	homepage = "http://maxconway.github.io/fbar/"
	cran = "fbar" 

	version("0.6.0", md5="f9d117b13cb966f9dde2c85618f7f8de")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-roi", type=("build", "run"))
	depends_on("r-roi-plugin-ecos", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
