# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlr(RPackage):
	"""Fuzzy Logic Rule Classifier

	FLR algorithm for classification
	"""
	
	cran = "FLR" 

	version("1.0", md5="2312028f1cb508db311beded66d7e7c6")

	depends_on("r-combinat", type=("build", "run"))
