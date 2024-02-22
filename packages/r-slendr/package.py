# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlendr(RPackage):
	"""A Simulation Framework for Spatiotemporal Population Genetics

	A framework for simulating spatially explicit genomic data which
    leverages real cartographic information for programmatic and visual encoding
    of spatiotemporal population dynamics on real geographic landscapes. Population
    genetic models are then automatically executed by the 'SLiM' software by Haller
    et al. (2019) <doi:10.1093/molbev/msy228> behind the scenes, using a custom
    built-in simulation 'SLiM' script. Additionally, fully abstract spatial models
    not tied to a specific geographic location are supported, and users can also
    simulate data from standard, non-spatial, random-mating models. These can be
    simulated either with the 'SLiM' built-in back-end script, or using an efficient
    coalescent population genetics simulator 'msprime' by Baumdicker et al. (2022)
    <doi:10.1093/genetics/iyab229> with a custom-built 'Python' script bundled with the
    R package. Simulated genomic data is saved in a tree-sequence format and can be
    loaded, manipulated, and summarised using tree-sequence functionality via an R
    interface to the 'Python' module 'tskit' by Kelleher et al. (2019)
    <doi:10.1038/s41588-019-0483-y>. Complete model configuration, simulation and
    analysis pipelines can be therefore constructed without a need to leave the R
    environment, eliminating friction between disparate tools for population genetic
    simulations and data analysis.
	"""
	
	homepage = "https://github.com/bodkan/slendr"
	cran = "slendr" 

	version("0.9.1", md5="4b7589f510533e3943fe2ffa02bc1017")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-ijtiff", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
