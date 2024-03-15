# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiomics(RPackage):
	"""Analysis of Omics Data in Observational Studies

	A collection of fast and flexible functions for analyzing
    omics data in observational studies. Multiple different approaches for
    integrating multiple environmental/genetic factors, omics data, and/or
    phenotype data are implemented. This includes functions for performing
    omics wide association studies with one or more variables of interest
    as the exposure or outcome; a function for performing a meet in the
    middle analysis for linking exposures, omics, and outcomes (as
    described by Chadeau-Hyam et al., (2010)
    <doi:10.3109/1354750X.2010.533285>); and a function for performing a
    mixtures analysis across all omics features using quantile-based
    g-Computation (as described by Keil et al., (2019)
    <doi:10.1289/EHP5838>).
	"""
	
	cran = "epiomics" 

	version("1.1.0", md5="0df81a8c56bb1c8f455925fa9717ba3f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-qgcomp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
