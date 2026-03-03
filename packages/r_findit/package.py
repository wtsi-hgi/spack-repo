# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFindit(RPackage):
	"""Finding Heterogeneous Treatment Effects

	The heterogeneous treatment effect estimation procedure 
        proposed by Imai and Ratkovic (2013)<DOI: 10.1214/12-AOAS593>.  
        The proposed method is applicable, for
        example, when selecting a small number of most (or least)
        efficacious treatments from a large number of alternative
        treatments as well as when identifying subsets of the
        population who benefit (or are harmed by) a treatment of
        interest. The method adapts the Support Vector Machine
        classifier by placing separate LASSO constraints over the
        pre-treatment parameters and causal heterogeneity parameters of
        interest. This allows for the qualitative distinction between
        causal and other parameters, thereby making the variable
        selection suitable for the exploration of causal heterogeneity. 	
        The package also contains a class of functions, CausalANOVA, 
        which estimates the average marginal interaction effects (AMIEs)
        by a regularized ANOVA as proposed by Egami and Imai (2019)<DOI:10.1080/01621459.2018.1476246>. 
        It contains a variety of regularization techniques to facilitate 
	analysis of large factorial experiments. 
	"""
	
	cran = "FindIt" 

	version("1.2.0", md5="192b01266924924008c18d7fba861b14")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-glinternet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
