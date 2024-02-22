# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmlbr(RPackage):
	"""Interface to the Penn Machine Learning Benchmarks Data
Repository

	Check available classification and regression data sets from the PMLB repository and download them.
    The PMLB repository (<https://github.com/EpistasisLab/pmlbr>) contains a curated collection of data sets for evaluating and comparing machine learning algorithms.
    These data sets cover a range of applications, and include binary/multi-class classification problems and 
    regression problems, as well as combinations of categorical, ordinal, and continuous features.
    There are currently over 150 datasets included in the PMLB repository.
	"""
	
	homepage = "https://github.com/EpistasisLab/pmlbr"
	cran = "pmlbr" 

	version("0.2.1", md5="f7cb5bae8f5cae2f0647b77af21dc73c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
