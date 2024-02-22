# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausaloptim(RPackage):
	"""An Interface to Specify Causal Graphs and Compute Bounds on
Causal Effects

	When causal quantities are not identifiable from the observed data, it still may be possible 
            to bound these quantities using the observed data. We outline a class of problems for which the 
            derivation of tight bounds is always a linear programming problem and can therefore, at least 
            theoretically, be solved using a symbolic linear optimizer. We extend and generalize the 
            approach of Balke and Pearl (1994) <doi:10.1016/B978-1-55860-332-5.50011-0> and we provide 
            a user friendly graphical interface for setting up such problems via directed acyclic 
            graphs (DAG), which only allow for problems within this class to be depicted. The user can 
            then define linear constraints to further refine their assumptions to meet their specific 
            problem, and then specify a causal query using a text interface. The program converts this 
            user defined DAG, query, and constraints, and returns tight bounds. The bounds can be 
            converted to R functions to evaluate them for specific datasets, and to latex code for 
            publication. The methods and proofs of tightness and validity of the bounds are described in
            a paper by Sachs, Jonzon, Gabriel, and Sjölander (2022) 
            <doi:10.1080/10618600.2022.2071905>.
	"""
	
	homepage = "https://github.com/sachsmc/causaloptim"
	cran = "causaloptim" 

	version("0.9.8", md5="7eff5ee6b1dfaea96de478e06ce208f5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
