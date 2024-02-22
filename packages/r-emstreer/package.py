# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmstreer(RPackage):
	"""Tools for Fast Computing and Visualizing Euclidean Minimum
Spanning Trees

	Fast and easily computes an Euclidean Minimum Spanning Tree (EMST) from data,
    relying on the R API for 'mlpack' - the C++ Machine Learning Library (Curtin et. al., 2013).
    'emstreeR' uses the Dual-Tree Boruvka (March, Ram, Gray, 2010, <doi:10.1145/1835804.1835882>), 
    which is theoretically and empirically the fastest algorithm for computing an EMST. This package also provides 
    functions and an S3 method for readily visualizing Minimum Spanning Trees (MST) using either the 
    style of the 'base', 'scatterplot3d', or 'ggplot2' libraries; and functions to export the MST output to shapefiles.
	"""
	
	cran = "emstreeR" 

	version("3.1.2", md5="8a7f2c09223c6d2f7577540f27065f32")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mlpack", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
