# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenotype(RPackage):
	"""A Tool for Phenotypic Data Processing

	Large-scale phenotypic data processing is essential in research. Researchers need to eliminate outliers from the data in order to obtain true and reliable results. Best linear unbiased prediction (BLUP) is a standard method for estimating random effects of a mixed model. This method can be used to process phenotypic data under different conditions and is widely used in animal and plant breeding. The 'Phenotype' can remove outliers from phenotypic data and performs the best linear unbiased prediction (BLUP), help researchers quickly complete phenotypic data analysis. H.P.Piepho. (2008) <doi:10.1007/s10681-007-9449-8>.
	"""
	
	homepage = "https://github.com/biozhp/Phenotype"
	cran = "Phenotype" 

	version("0.1.0", md5="87c490cc7868c6b691b99122c773f749")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
