# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfmm(RPackage):
	"""Latent Factor Mixed Models

	Fast and accurate inference of 
             gene-environment associations (GEA) in genome-wide studies 
             (Caye et al., 2019, <doi:10.1093/molbev/msz008>). 
             We developed a least-squares estimation approach for confounder and effect sizes 
             estimation that provides a unique framework for several categories of genomic data, 
             not restricted to genotypes. 
             The speed of the new algorithm is several times faster than the existing GEA approaches, 
             then our previous version of the 'LFMM' program present in the 'LEA' package 
             (Frichot and Francois, 2015, <doi:10.1111/2041-210X.12382>).
	"""
	
	cran = "lfmm" 

	version("1.1", md5="55d095d16fb9e51b08cb09523385548b")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
