# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMri(RPackage):
	"""Modified Rand and Wallace Indices

	It provides functions to compute the values of different modifications of the Rand and Wallace indices. The indices are used to measure the stability or similarity of two partitions obtained on two different sets of units with a non-empty intercept. Splitting and merging of clusters can (depends on the selected index) have a different effect on the value of the indices.  The indices are proposed in Cugmas and Ferligoj (2018) <http://ibmi.mf.uni-lj.si/mz/2018/no-1/Cugmas2018.pdf>.
	"""
	
	cran = "mri" 

	version("1.0.1", md5="a15827bb88aea72751bc3934e0218b58")

	depends_on("r@3.1:", type=("build", "run"))
