# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvmpath(RPackage):
	"""The SVM Path Algorithm

	Computes the entire regularization path for the two-class svm classifier
		with essentially the same cost as a single SVM fit.
	"""
	
	homepage = "http://www.jmlr.org/papers/volume5/hastie04a/hastie04a.pdf"
	cran = "svmpath" 

	version("0.970", md5="f9fd81e0913063cbf7a0e7a97b3c2e6f")

	depends_on("r-kernlab", type=("build", "run"))
