# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProjectionbasedclustering(RPackage):
	"""Projection Based Clustering

	A clustering approach applicable to every projection method is proposed here. The two-dimensional scatter plot of any projection method can construct a topographic map which displays unapparent data structures by using distance and density information of the data. The generalized U*-matrix renders this visualization in the form of a topographic map, which can be used to automatically define the clusters of high-dimensional data. The whole system is based on Thrun and Ultsch, "Using Projection based Clustering to Find Distance and Density based Clusters in High-Dimensional Data" <DOI:10.1007/s00357-020-09373-2>. Selecting the correct projection method will result in a visualization in which mountains surround each cluster. The number of clusters can be determined by counting valleys on the topographic map. Most projection methods are wrappers for already available methods in R. By contrast, the neighbor retrieval visualizer (NeRV) is based on C++ source code of the 'dredviz' software package, the t-SNE multicore version is based on C++ source code of Dmitry Ulyanov, and the Curvilinear Component Analysis (CCA) is translated from 'MATLAB' ('SOM Toolbox' 2.0) to R.
	"""
	
	homepage = "https://www.deepbionics.org"
	cran = "ProjectionBasedClustering" 

	version("1.2.1", md5="e5c5112f7c0331f199d78df154ac6789")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-generalizedumatrix", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
