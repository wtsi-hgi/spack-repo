# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdenica(RPackage):
	"""Product Density Estimation for ICA using Tilted Gaussian Density
Estimates

	A direct and flexible method for estimating an ICA model. This approach estimates the densities for each component directly via a tilted Gaussian. The tilt functions are estimated via a GAM Poisson model. Details can be found in "Elements of Statistical Learning (2nd Edition)" in Section 14.7.4.
	"""
	
	homepage = "https://hastie.su.domains/ElemStatLearn/printings/ESLII_print12_toc.pdf"
	cran = "ProDenICA" 

	version("1.1", md5="7c389c8cfe4fd44d8570e2bed6d7e867")

	depends_on("r-gam", type=("build", "run"))
