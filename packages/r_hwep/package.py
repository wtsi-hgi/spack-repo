# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHwep(RPackage):
	"""Hardy-Weinberg Equilibrium in Polyploids

	Inference concerning equilibrium and random mating in 
    autopolyploids. Methods are available to test for equilibrium 
    and random mating at any even ploidy level (>2) in the presence
    of double reduction at biallelic loci. For autopolyploid populations
    in equilibrium, methods are available to estimate the degree of 
    double reduction. We also provide functions to calculate genotype 
    frequencies at equilibrium, or after one or several rounds of 
    random mating, given rates of double reduction. The main function is
    hwefit(). This material is based upon work supported by the
    National Science Foundation under Grant No. 2132247. The opinions,
    findings, and conclusions or recommendations expressed are those of
    the author and do not necessarily reflect the views of the National
    Science Foundation. For details of these methods, see 
    Gerard (2022a) <doi:10.1111/biom.13722> and
    Gerard (2022b) <doi:10.1101/2022.08.11.503635>.
	"""
	
	homepage = "https://dcgerard.github.io/hwep/"
	cran = "hwep" 

	version("2.0.2", md5="bc91cea3f3525915862dd329e5c1eaf0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.2:", type=("build", "run"))
	depends_on("r-tensr", type=("build", "run"))
	depends_on("r-updog", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
