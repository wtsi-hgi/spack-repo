# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJgl(RPackage):
	"""Performs the Joint Graphical Lasso for Sparse Inverse Covariance
Estimation on Multiple Classes

	The Joint Graphical Lasso is a generalized method for
        estimating Gaussian graphical models/ sparse inverse covariance
        matrices/ biological networks on multiple classes of data.  We
        solve JGL under two penalty functions: The Fused Graphical
        Lasso (FGL), which employs a fused penalty to encourage inverse
        covariance matrices to be similar across classes, and the Group
        Graphical Lasso (GGL), which encourages similar network
        structure between classes.  FGL is recommended over GGL for
        most applications. Reference: Danaher P, Wang P, Witten DM. (2013) 
        <doi:10.1111/rssb.12033>.
	"""
	
	cran = "JGL" 

	version("2.3.2", md5="447ddb57e875fb6b2f46fb8d6f5ef129")

	depends_on("r-igraph", type=("build", "run"))
