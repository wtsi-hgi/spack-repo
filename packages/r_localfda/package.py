# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLocalfda(RPackage):
	"""Localization Processes for Functional Data Analysis

	Implementation of a theoretically supported alternative to k-nearest neighbors for functional data 
  to solve problems of estimating unobserved segments of a partially observed functional data sample, 
  functional classification and outlier detection. The approximating neighbor curves are piecewise functions built from a functional sample. 
  Instead of a distance on a function space we use a locally defined distance function that satisfies stabilization criteria. 
  The package allows the implementation of the methodology and the replication of the results in Elías, A., Jiménez, R. and Yukich, J. (2020) <arXiv:2007.16059>.
	"""
	
	homepage = "https://github.com/aefdz/localFDA"
	cran = "localFDA" 

	version("1.0.0", md5="2c65e133b6324b3c1f147f45c85fa8c1")

	depends_on("r@2.10:", type=("build", "run"))
