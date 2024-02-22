# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmixtcompio(RPackage):
	"""Minimal Interface of the C++ 'MixtComp' Library for Mixture
Models with Heterogeneous and (Partially) Missing Data

	Mixture Composer <https://github.com/modal-inria/MixtComp> is a project to build mixture models with
    heterogeneous data sets and partially missing data management.
    It includes models for real, categorical, counting, functional and ranking data.
    This package contains the minimal R interface of the C++ 'MixtComp' library.
	"""
	
	homepage = "https://github.com/modal-inria/MixtComp"
	cran = "RMixtCompIO" 

	version("4.0.11", md5="13fad6660ee4639f9e0b3c07d5a98715")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
