# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmpiricalbrownsmethod(RPackage):
	"""Uses Brown's method to combine p-values from dependent tests

	Combining P-values from multiple statistical tests is common in bioinformatics. However, this procedure is non-trivial for dependent P-values. This package implements an empirical adaptation of Brown’s Method (an extension of Fisher’s Method) for combining dependent P-values which is appropriate for highly correlated data sets found in high-throughput biological experiments.
	"""
	
	homepage = "https://github.com/IlyaLab/CombiningDependentPvaluesUsingEBM.git"
	bioc = "EmpiricalBrownsMethod"

	version("1.36.0", commit="2a598f8048f99de6cd53d6874c6d8d501381f9c9")
	version("1.30.0", commit="7d9465f2445e8f15009afad0888603f222ed2f0a")

	depends_on("r@3.2:", type=("build", "run"))
