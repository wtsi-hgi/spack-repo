# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepthtools(RPackage):
	"""Depth Tools Package

	Implementation of different statistical tools for the 
        description and analysis of gene expression data based on the 
        concept of data depth, namely, the scale curves for 
        visualizing the dispersion of one or various groups of samples 
        (e.g. types of tumors), a rank test to decide whether two groups 
        of samples come from a single distribution and two methods of
        supervised classification techniques, the DS and TAD methods. 
        All these techniques are based on the Modified Band Depth, which
        is a recent notion of depth with a low computational cost, what 
        renders it very appropriate for high dimensional data such as 
        gene expression data.
	"""
	
	cran = "depthTools" 

	version("0.7", md5="04de86c2f7a47c5143234c1368d59836")

	depends_on("r@2.8:", type=("build", "run"))
