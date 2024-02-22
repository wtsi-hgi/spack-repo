# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurelda(RPackage):
	"""A Novel Multi-Disease Automated Phenotyping Method for the EHR

	A statistical learning method to simultaneously predict a range of target phenotypes using codified and natural language processing (NLP)-derived Electronic Health Record (EHR) data. See Ahuja et al (2020) JAMIA <doi:10.1093/jamia/ocaa079> for details.
	"""
	
	homepage = "https://github.com/celehs/sureLDA"
	cran = "sureLDA" 

	version("0.1.0-1", md5="462bc86f8df0a27336a29f112195ed13")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-map", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
