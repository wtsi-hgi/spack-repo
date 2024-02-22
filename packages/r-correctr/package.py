# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrectr(RPackage):
	"""Corrected Test Statistics for Comparing Machine Learning Models
on Correlated Samples

	Calculate a set of corrected test statistics for cases when samples
    are not independent, such as when classification accuracy values are obtained
    over resamples or through k-fold cross-validation, as proposed by Nadeau and Bengio (2003) <doi:10.1023/A:1024068626366> 
    and presented in Bouckaert and Frank (2004) <doi:10.1007/978-3-540-24775-3_3>.
	"""
	
	homepage = "https://hendersontrent.github.io/correctR/"
	cran = "correctR" 

	version("0.1.3", md5="58e50e4232edb65e7149c8cdf8c9a5db")

	depends_on("r@3.5:", type=("build", "run"))
