# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimer(RPackage):
	"""Data Simulation for Life Science and Breeding

	Data simulator including genotype, phenotype, pedigree, 
    selection and reproduction in R. It simulates most of reproduction process
    of animals or plants and provides data for GS (Genomic Selection),
    GWAS (Genome-Wide Association Study), and Breeding.
    For ADI model, please see Kao C and Zeng Z (2002) <doi:10.1093/genetics/160.3.1243>.
    For build.cov, please see B. D. Ripley (1987) <ISBN:9780470009604>.
	"""
	
	homepage = "https://github.com/xiaolei-lab/SIMER"
	cran = "simer" 

	version("0.9.0.4", md5="0431de02e7824198e7ff73bce956d932")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
