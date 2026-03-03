# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimensio(RPackage):
	"""Multivariate Data Analysis

	Simple Principal Components Analysis (PCA) and (Multiple)
    Correspondence Analysis (CA) based on the Singular Value Decomposition
    (SVD). This package provides S4 classes and methods to compute,
    extract, summarize and visualize results of multivariate data
    analysis. It also includes methods for partial bootstrap validation
    described in Greenacre (1984, ISBN: 978-0-12-299050-2) and Lebart et
    al. (2006, ISBN: 978-2-10-049616-7).
	"""
	
	homepage = "https://packages.tesselle.org/dimensio/"
	cran = "dimensio" 

	version("0.6.0", md5="536b1d7cef5a168a5ab47bb050de7fcb")
	version("0.5.0", md5="3160e4e34e13d94bff36ea6bccffb8b5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-arkhe@1.6:", type=("build", "run"))
