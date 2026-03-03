# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPweall(RPackage):
	"""Design and Monitoring of Survival Trials Accounting for Complex
Situations

	Calculates various functions needed for design and monitoring survival trials
    accounting for complex situations such as delayed treatment effect, treatment crossover, non-uniform accrual,
    and different censoring distributions between groups. The event time distribution is assumed to be
    piecewise exponential (PWE) distribution and the entry time is assumed to be piecewise uniform distribution.
    As compared with Version 1.2.1, two more types of hybrid crossover are added. 
    A bug is corrected in the function "pwecx" that calculates the crossover-adjusted survival, distribution, 
    density, hazard and cumulative hazard functions. 
    Also, to generate the crossover-adjusted event time random variable,  a more efficient 
    algorithm is used and the output includes crossover indicators. 
	"""
	
	cran = "PWEALL" 

	version("1.3.0.1", md5="cb59be19d113a876be776beb0ee2ea6f")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
