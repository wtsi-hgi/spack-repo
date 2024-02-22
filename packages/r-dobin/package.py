# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDobin(RPackage):
	"""Dimension Reduction for Outlier Detection

	A dimension reduction technique for outlier detection. DOBIN: a Distance 
    based Outlier BasIs using Neighbours, constructs a set of basis vectors for outlier 
    detection. This is not an outlier detection method; rather it is a pre-processing 
    method for outlier detection. It brings outliers to the fore-front using fewer basis 
    vectors (Kandanaarachchi, Hyndman 2020) <doi:10.1080/10618600.2020.1807353>. 
	"""
	
	homepage = "https://sevvandi.github.io/dobin/"
	cran = "dobin" 

	version("1.0.4", md5="07719554220b4b8a665da375d36fd198")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
