# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REff2(RPackage):
	"""Efficient Least Squares for Total Causal Effects

	Estimate a total causal effect from observational data under 
    linearity and causal sufficiency. The observational data is supposed to 
    be generated from a linear structural equation model (SEM) with independent 
    and additive noise. The underlying causal DAG associated the SEM is required
    to be known up to a maximally oriented partially directed graph (MPDAG), 
    which is a general class of graphs consisting of both directed and 
    undirected edges, including CPDAGs (i.e., essential graphs) and DAGs. Such
    graphs are usually obtained with structure learning algorithms with added 
    background knowledge. The program is able to estimate every identified 
    effect, including single and multiple treatment variables. Moreover, the 
    resulting estimate has the minimal asymptotic covariance (and hence 
    shortest confidence intervals) among all estimators that are based on the 
    sample covariance. 
	"""
	
	homepage = "https://github.com/richardkwo/eff2"
	cran = "eff2" 

	version("1.0.2", md5="01e71bd802ee24ab5c2fb807f51c626c", url="https://cran.r-project.org/src/contrib/eff2_1.0.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pcalg@2.6:", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
