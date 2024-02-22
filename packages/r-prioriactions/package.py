# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrioriactions(RPackage):
	"""Multi-Action Conservation Planning

	This uses a mixed integer mathematical programming (MIP)
        approach for building and solving multi-action planning problems, 
        where the goal is to find an optimal combination of management actions that
        abate threats, in an efficient way while accounting for spatial aspects. 
        Thus, optimizing the connectivity and conservation effectiveness of 
        the prioritized units and of the deployed actions. The package is capable of 
        handling different commercial (gurobi, CPLEX) and non-commercial (symphony, CBC) MIP solvers. 
        Gurobi optimization solver can be installed using comprehensive instructions in 
        the 'gurobi' installation vignette of the prioritizr package (available in 
        <https://prioritizr.net/articles/gurobi_installation_guide.html>). Instead, 'CPLEX'
        optimization solver can be obtain from IBM CPLEX web page (available here 
        <https://www.ibm.com/es-es/products/ilog-cplex-optimization-studio>). Additionally, 
        the 'rcbc' R package (available at
    <https://github.com/dirkschumacher/rcbc>) can be used to obtain solutions
    using the CBC optimization software (<https://github.com/coin-or/Cbc>). Methods used in the 
        package refers to Salgado-Rojas et al. (2020) <doi:10.1016/j.ecolmodel.2019.108901>,
        Beyer et al. (2016) <doi:10.1016/j.ecolmodel.2016.02.005>, Cattarino et al. (2015)
        <doi:10.1371/journal.pone.0128027> and Watts et al. (2009) <doi:10.1016/j.envsoft.2009.06.005>. 
        See the prioriactions website for more information, documentations and examples.
	"""
	
	homepage = "https://prioriactions.github.io/prioriactions/"
	cran = "prioriactions" 

	version("0.5.0", md5="58841d03941d0316e2a69e052ab14818")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-proto", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
