# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGglasso(RPackage):
	"""Group Lasso Penalized Learning Using a Unified BMD Algorithm

	A unified algorithm, blockwise-majorization-descent (BMD), for efficiently computing the solution paths of the group-lasso penalized least squares, logistic regression, Huberized SVM and squared SVM. The package is an implementation of Yang, Y. and Zou, H. (2015) DOI: <doi:10.1007/s11222-014-9498-5>.
	"""
	
	homepage = "https://github.com/emeryyi/gglasso"
	cran = "gglasso" 

	version("1.5.1", md5="bbe0ed2d22fd91f973a421d7192d6473")
	version("1.5", md5="542bbd4eb7f6d4663c141c12414da19a")

