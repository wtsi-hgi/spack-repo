# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBlsm(RPackage):
	"""Bayesian Latent Space Model

	Provides a Bayesian latent space 
    model for complex networks, either weighted or unweighted.
    Given an observed input graph, the estimates for the latent coordinates 
    of the nodes are obtained through a Bayesian MCMC algorithm. 
    The overall likelihood of the graph depends on a fundamental probability 
    equation, which is defined so that ties are more likely to exist 
    between nodes whose latent space coordinates are close. 
    The package is mainly based on the model by Hoff, Raftery and Handcock (2002)
    <doi:10.1198/016214502388618906> and contains some extra features 
    (e.g., removal of the Procrustean step, weights implemented as 
    coefficients of the latent distances, 3D plots). 
    The original code related to the above model was retrieved from
    <https://www.stat.washington.edu/people/pdhoff/Code/hoff_raftery_handcock_2002_jasa/>.
    Users can inspect the MCMC simulation, create and customize insightful 
    graphical representations or apply clustering techniques. 
	"""
	
	cran = "BLSM" 

	version("0.1.0", md5="76d9d442c0053285de4a4d7154693377")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
