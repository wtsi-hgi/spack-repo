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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EmpiricalBrownsMethod_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EmpiricalBrownsMethod/EmpiricalBrownsMethod_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="ef6c792f67abc45ca4ad4bf3bc1e7c3dfa7dd4368a33ddc3ae32635243043a0f")

	depends_on("r@3.2:", type=("build", "run"))
