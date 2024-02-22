# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadplexr(RPackage):
	"""Analysis of Multiplex Cytometric Bead Assays

	Reproducible and automated analysis of multiplex bead assays such
    as CBA (Morgan et al. 2004; <doi: 10.1016/j.clim.2003.11.017>), LEGENDplex
    (Yu et al. 2015; <doi: 10.1084/jem.20142318>), and MACSPlex (Miltenyi
    Biotec 2014; Application note: Data acquisition and analysis without the
    MACSQuant analyzer;
    <https://www.miltenyibiotec.com/upload/assets/IM0021608.PDF>). The
    package provides functions for streamlined reading of fcs files, and
    identification of bead clusters and analyte expression. The package eases
    the calculation of standard curves and the subsequent calculation of the
    analyte concentration.
	"""
	
	homepage = "https://gitlab.com/ustervbo/beadplexr"
	cran = "beadplexr" 

	version("0.5.0", md5="26463462c2b2a58a783e6447899ef950")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-drc", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
