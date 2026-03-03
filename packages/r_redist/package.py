# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRedist(RPackage):
	"""Simulation Methods for Legislative Redistricting

	Enables researchers to sample redistricting plans from a pre-specified
    target distribution using Sequential Monte Carlo and Markov Chain Monte Carlo
    algorithms. The package allows for the implementation of various constraints in
    the redistricting process such as geographic compactness and population parity
    requirements. Tools for analysis such as computation of various summary statistics
    and plotting functionality are also included. The package implements the SMC 
    algorithm of McCartan and Imai (2023) <doi:10.1214/23-AOAS1763>, the enumeration 
    algorithm of Fifield, Imai, Kawahara, and Kenny (2020) <doi:10.1080/2330443X.2020.1791773>,
    the Flip MCMC algorithm of Fifield, Higgins, Imai and Tarr (2020) <doi:10.1080/10618600.2020.1739532>,
    the Merge-split/Recombination algorithms of Carter et al. (2019) <arXiv:1911.01503> 
    and DeFord et al. (2021) <doi:10.1162/99608f92.eb30390f>, and the Short-burst 
    optimization algorithm of Cannon et al. (2020) <arXiv:2011.02288>.
	"""
	
	homepage = "https://alarm-redist.org/redist/"
	cran = "redist" 

	version("4.2.0", md5="ffaba15e1fce1c6d2b3b712eb1e91aec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-redistmetrics", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-servr", type=("build", "run"))
	depends_on("r-sys", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
	depends_on("python", type=("build", "link", "run"))
