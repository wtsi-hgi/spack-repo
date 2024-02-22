# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhylogeneticem(RPackage):
	"""Automatic Shift Detection using a Phylogenetic EM

	
    Implementation of the automatic shift detection method for
    Brownian Motion (BM) or Ornstein–Uhlenbeck (OU) models of trait evolution on
    phylogenies. Some tools to handle equivalent shifts configurations are also
    available. See Bastide et al. (2017) <doi:10.1111/rssb.12206> and
    Bastide et al. (2018) <doi:10.1093/sysbio/syy005>.
	"""
	
	homepage = "https://github.com/pbastide/PhylogeneticEM"
	cran = "PhylogeneticEM" 

	version("1.7.0", md5="3e1f0dd92d22e493863a82581e7b9d8a")

	depends_on("r-ape@5.3:", type=("build", "run"))
	depends_on("r-matrix@1.2.18:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-capushe@1.1.1:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-gglasso@1.4:", type=("build", "run"))
	depends_on("r-glmnet@2.0.5:", type=("build", "run"))
	depends_on("r-linselect@1.1.1:", type=("build", "run"))
	depends_on("r-mass@7.3.45:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-robustbase@0.92.6:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
