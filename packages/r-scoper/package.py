# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoper(RPackage):
	"""Spectral Clustering-Based Method for Identifying B Cell Clones

	Provides a computational framework for identification of B cell clones from 
             Adaptive Immune Receptor Repertoire sequencing (AIRR-Seq) data. Three main 
             functions are included (identicalClones, hierarchicalClones, and spectralClones) 
             that perform clustering among sequences of BCRs/IGs (B cell receptors/immunoglobulins) 
             which share the same V gene, J gene and junction length.
             Nouri N and Kleinstein SH (2018) <doi: 10.1093/bioinformatics/bty235>.
             Nouri N and Kleinstein SH (2019) <doi: 10.1101/788620>.
             Gupta NT, et al. (2017) <doi: 10.4049/jimmunol.1601850>.
	"""
	
	homepage = "https://scoper.readthedocs.io"
	cran = "scoper" 

	version("1.3.0", md5="49fd80d0b726ad1839781b786549420d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-alakazam@1.3:", type=("build", "run"))
	depends_on("r-shazam@1.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
