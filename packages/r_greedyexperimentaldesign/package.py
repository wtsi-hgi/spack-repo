# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGreedyexperimentaldesign(RPackage):
	"""Greedy Experimental Design Construction

	Computes experimental designs for a
    two-arm experiment with covariates via a number of methods:
    (0) complete randomization and randomization with forced-balance,
    (1) Greedily optimizing a
    balance objective function via pairwise switching. This optimization 
    provides lower variance for the treatment effect estimator (and higher 
    power) while preserving a design that is close to complete randomization.
    We return all iterations of the designs for use in a permutation test,
    (2) The second is via numerical optimization 
    (via 'gurobi' which must be installed, see <https://www.gurobi.com/documentation/9.1/quickstart_windows/r_ins_the_r_package.html>) 
    a la Bertsimas and Kallus, 
    (3) rerandomization, 
    (4) Karp's method for one covariate, 
    (5) exhaustive enumeration to find the 
    optimal solution (only for small sample sizes),
    (6) Binary pair matching using the 'nbpMatching' library,
    (7) Binary pair matching plus design number (1) to further optimize balance,
    (8) Binary pair matching plus design number (3) to further optimize balance,
    (9) Hadamard designs,
    (10) Simultaneous Multiple Kernels.
    In (1-9) we allow for three objective functions:
    Mahalanobis distance,
    Sum of absolute differences standardized and
    Kernel distances via the 'kernlab' library. This package is the result of a stream of research that can be found in 
    Krieger, A, Azriel, D and Kapelner, A "Nearly Random Designs with Greatly Improved Balance" (2016) <arXiv:1612.02315>,
    Krieger, A, Azriel, D and Kapelner, A "Better Experimental Design by Hybridizing Binary Matching with Imbalance 
    Optimization" (2021) <arXiv:2012.03330>.
	"""
	
	homepage = "https://github.com/kapelner/GreedyExperimentalDesign"
	cran = "GreedyExperimentalDesign" 

	version("1.5.6.1", md5="477091060eadca93681ff0bfefc6fd52")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rjava@0.9.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-nbpmatching", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("openjdk@1.7:", type=("build", "link", "run"))
