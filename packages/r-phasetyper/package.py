# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhasetyper(RPackage):
	"""General-Purpose Phase-Type Functions

	General implementation of core function from phase-type
    theory. 'PhaseTypeR' can be used to model continuous and discrete
    phase-type distributions, both univariate and multivariate. The
    package includes functions for outputting the mean and (co)variance of
    phase-type distributions; their density, probability and quantile
    functions; functions for random draws; functions for
    reward-transformation; and functions for plotting the distributions as
    networks. For more information on these functions please refer to
    Bladt and Nielsen (2017, ISBN: 978-1-4939-8377-3) and Campillo Navarro
    (2019)
    <https://orbit.dtu.dk/en/publications/order-statistics-and-multivariate-discrete-phase-type-distributio>.
	"""
	
	homepage = "https://rivasiker.github.io/PhaseTypeR/"
	cran = "PhaseTypeR" 

	version("1.0.4", md5="d9c53564965abef1f7fcdb18c169e810")

	depends_on("r-expm", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
