# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdetector(RPackage):
	"""Outlier Detection Using Partitioning Clustering Algorithms

	An object is called "outlier" if it remarkably deviates from the other objects in a data set. Outlier detection is the process to find outliers by using the methods that are based on distance measures, clustering and spatial methods (Ben-Gal, 2005 <ISBN 0-387-24435-2>). It is one of the intensively studied research topics for identification of novelties, frauds, anomalies, deviations or exceptions in addition to its use for outlier removing in data processing. This package provides the implementations of some novel approaches to detect the outliers based on typicality degrees that are obtained with the soft partitioning clustering algorithms such as Fuzzy C-means and its variants.
	"""
	
	homepage = "https://github.com/zcebeci/odetector"
	cran = "odetector" 

	version("1.0.1", md5="96ea70728cfd56fb9dad0843ee0bb971")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ppclust", type=("build", "run"))
