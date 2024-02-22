# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvmapit(RPackage):
	"""Multivariate Genome Wide Marginal Epistasis Test

	Epistasis, commonly defined as the interaction between genetic
  loci, is known to play an important role in the phenotypic variation of
  complex traits. As a result, many statistical methods have been developed to
  identify genetic variants that are involved in epistasis, and nearly all of
  these approaches carry out this task by focusing on analyzing one trait at a
  time. Previous studies have shown that jointly modeling multiple phenotypes
  can often dramatically increase statistical power for association mapping. In
  this  package, we present the 'multivariate MArginal ePIstasis Test'
  ('mvMAPIT') – a multi-outcome generalization of a recently proposed epistatic
  detection method which seeks to detect marginal epistasis or the combined
  pairwise interaction effects between a given variant and all other variants.
  By searching for marginal epistatic effects, one can identify genetic variants
  that are involved in epistasis without the need to identify the exact
  partners with which the variants interact – thus, potentially alleviating
  much of the statistical and computational burden associated with conventional
  explicit search based methods. Our proposed 'mvMAPIT' builds upon this
  strategy by taking advantage of correlation structure between traits to
  improve the identification of variants involved in epistasis.
  We formulate 'mvMAPIT' as a  multivariate linear mixed model and develop a
  multi-trait variance component estimation algorithm for efficient parameter
  inference and P-value computation. Together with reasonable model
  approximations, our proposed approach is scalable to moderately sized
  genome-wide association studies.
  Crawford et al. (2017) <doi:10.1371/journal.pgen.1006869>.
  Stamp et al. (2023) <doi:10.1093/g3journal/jkad118>.
	"""
	
	homepage = "https://github.com/lcrawlab/mvMAPIT"
	cran = "mvMAPIT" 

	version("2.0.3", md5="c9484a9567003a7c10b021c7ade08581")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-compquadform", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-harmonicmeanp", type=("build", "run"))
	depends_on("r-logging", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcppspdlog", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
