# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvchargcost(RPackage):
	"""Computes and Plot the Optimal Charging Strategy for Electric
Vehicles

	The purpose of this library is to compute the optimal charging cost function for a electric vehicle (EV). It is well known that the charging function of a EV is a concave function that can be approximated by a piece-wise linear function, so bigger the state of charge, slower the charging process is. Moreover, the other important function is the one that gives the electricity price. This function is usually step-wise, since depending on the time of the day, the price of the electricity is different. Then, the problem of charging an EV to a certain state of charge is not trivial. This library implements an algorithm to compute the optimal charging cost function, that is, it plots for a given state of charge r (between 0 and 1) the minimum cost we need to pay in order to charge the EV to that state of charge r. The details of the algorithm are described in González-Rodríguez et at (2023) <https://inria.hal.science/hal-04362876v1>.
	"""
	
	cran = "EVchargcost" 

	version("0.1.0", md5="f88ed56e5049e1ebb9d01eeae28d8fce")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
