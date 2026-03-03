# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbest(RPackage):
	"""R Bayesian Evidence Synthesis Tools

	Tool-set to support Bayesian evidence synthesis.  This
    includes meta-analysis, (robust) prior derivation from historical
    data, operating characteristics and analysis (1 and 2 sample
    cases). Please refer to Weber et al. (2021) <doi:10.18637/jss.v100.i19>
    for details on applying this package while Neuenschwander et al. (2010)
    <doi:10.1177/1740774509356002> and Schmidli et al. (2014)
    <doi:10.1111/biom.12242> explain details on the methodology.
	"""
	
	homepage = "https://opensource.nibr.com/RBesT/"
	cran = "RBesT" 

	version("1.7-3", md5="a69c6d551c836ca4cb990793157aacf5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-bayesplot@1.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-bh@1.72:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
	depends_on("pngquant", type=("build", "link", "run"))
