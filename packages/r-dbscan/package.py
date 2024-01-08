# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RDbscan(RPackage):
	"""Density-Based Spatial Clustering of Applications with Noise
(DBSCAN) and Related Algorithms

	A fast reimplementation of several density-based algorithms of
    the DBSCAN family. Includes the clustering algorithms DBSCAN (density-based 
    spatial clustering of applications with noise) and HDBSCAN (hierarchical 
    DBSCAN), the ordering algorithm OPTICS (ordering points to identify the 
    clustering structure), shared nearest neighbor clustering, and the outlier 
    detection algorithms LOF (local outlier factor) and GLOSH (global-local 
    outlier score from hierarchies). The implementations use the kd-tree data 
    structure (from library ANN) for faster k-nearest neighbor search. An R 
    interface to fast kNN and fixed-radius NN search is also provided. 
    Hahsler, Piekenbrock and Doran (2019) <doi:10.18637/jss.v091.i01>.
	"""
	
	homepage = "https://github.com/mhahsler/dbscan"
	cran = "dbscan" 

	version("1.1-11", md5="5ea8954540e20586e72890099e4ce214")

	depends_on("r-rcpp@1.0.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
