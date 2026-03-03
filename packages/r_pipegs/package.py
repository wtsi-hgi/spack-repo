# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPipegs(RPackage):
	"""Permutation p-Value Estimation for Gene Set Tests

	Code for various permutation p-values estimation methods for gene set test. The description of corresponding methods can be found in the dissertation of Yu He(2016) "Efficient permutation P-value estimation for gene set tests" <https://searchworks.stanford.edu/view/11849351>. One of the methods also corresponds to the paper "Permutation p-value approximation via generalized Stolarsky invariance" <arXiv:1603.02757>.
	"""
	
	homepage = "https://searchworks.stanford.edu/view/11849351"
	cran = "pipeGS" 

	version("0.4", md5="703739ccbdd8e7d6a43a42e993007482")

