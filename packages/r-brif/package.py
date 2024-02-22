# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrif(RPackage):
	"""A Tree and Forest Tool for Classification and Regression

	Build decision trees and random forests for classification and regression. The implementation strikes a balance between minimizing computing efforts and maximizing the expected predictive accuracy, thus scales well to large data sets. Multi-threading is available through 'OpenMP' <https://gcc.gnu.org/wiki/openmp>.  
	"""
	
	cran = "brif" 

	version("1.4.1", md5="a2bdd50aa70344b21ec62d85efbddc94")

	depends_on("r-rcpp", type=("build", "run"))
