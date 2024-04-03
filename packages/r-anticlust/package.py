# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnticlust(RPackage):
	"""Subset Partitioning via Anticlustering

	The method of anticlustering partitions a pool of elements
	into groups (i.e., anticlusters) with the goal of maximizing
	between-group similarity or within-group heterogeneity.  The
	anticlustering approach thereby reverses the logic of cluster analysis
	that strives for high within-group homogeneity and clear separation
	between groups.  Computationally, anticlustering is accomplished by
	maximizing instead of minimizing a clustering objective function, such
	as the intra-cluster variance (used in k-means clustering) or the sum
	of pairwise distances within clusters. The main function
	anticlustering() gives access to exact and heuristic anticlustering
	methods described in Papenberg and Klau (2021;
	<doi:10.1037/met0000301>), Brusco et al. (2020;
	<doi:10.1111/bmsp.12186>), and Papenberg (2023;
	<doi:10.1111/bmsp.12315>). The exact algorithms require that an
	integer linear programming solver is installed, either the GNU linear
	programming kit (<https://www.gnu.org/software/glpk/glpk.html>)
	together with the interface package 'Rglpk'
	(<https://cran.R-project.org/package=Rglpk>), or the SYMPHONY ILP
	solver (<https://github.com/coin-or/SYMPHONY>) together with the
	interface package 'Rsymphony'
	(<https://cran.r-project.org/package=Rsymphony>). Full access to the
	bicriterion anticlustering method proposed by Brusco et al. (2020) is
	given via the function bicriterion_anticlustering(), while
	kplus_anticlustering() implements the full functionality of the k-plus
	anticlustering approach proposed by Papenberg (2023). Some other
	functions are available to solve classical clustering problems. The
	function balanced_clustering() applies a cluster analysis under size
	constraints, i.e., creates equal-sized clusters. The function
	matching() can be used for (unrestricted, bipartite, or K-partite)
	matching. The function wce() can be used optimally solve the
	(weighted) cluster editing problem, also known as correlation
	clustering, clique partitioning problem or transitivity clustering.
	"""
	
	homepage = "https://github.com/m-Py/anticlust"
	cran = "anticlust"

	version("0.8.1", md5="f4f88e3a48586d8511855367f123cee0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rann@2.6:", type=("build", "run"))
	depends_on("glpk+gmp", type=("build", "link", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
