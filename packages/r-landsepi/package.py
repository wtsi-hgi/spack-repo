# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandsepi(RPackage):
	"""Landscape Epidemiology and Evolution

	A stochastic, spatially-explicit, demo-genetic model simulating the spread and evolution 
    of a plant pathogen in a heterogeneous landscape to assess resistance deployment strategies. 
    It is based on a spatial geometry for describing the landscape and allocation of different cultivars, 
    a dispersal kernel for the dissemination of the pathogen, and a SEIR 
    ('Susceptible-Exposed-Infectious-Removed’) structure with a discrete time step.
    It provides a useful tool to assess the performance of a wide range of deployment options with 
    respect to their epidemiological, evolutionary and economic outcomes.
    Loup Rimbaud, Julien Papaïx, Jean-François Rey, Luke G Barrett, 
    Peter H Thrall (2018) <doi:10.1371/journal.pcbi.1006067>.
	"""
	
	homepage = "https://csiro-inra.pages.biosp.inrae.fr/landsepi/"
	cran = "landsepi" 

	version("1.4.0", md5="a0c7356c690264b83a2a461e993f37bb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sp@1.0.17:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.3.0:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
