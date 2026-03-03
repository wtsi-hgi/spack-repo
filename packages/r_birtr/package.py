# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBirtr(RPackage):
	"""The R Package for "The Basics of Item Response Theory Using R"

	R functions for "The Basics of Item Response Theory Using R" by Frank B. Baker and Seock-Ho Kim (Springer, 2017, ISBN-13: 978-3-319-54204-1) including iccplot(), icccal(), icc(), iccfit(), groupinv(), tcc(), ability(), tif(), and rasch().  For example, iccplot() plots an item characteristic curve under the two-parameter logistic model.
	"""
	
	cran = "birtr" 

	version("1.0.0", md5="5093205af30d510d564de04d34e65de7")

	depends_on("r@3.4.1:", type=("build", "run"))
