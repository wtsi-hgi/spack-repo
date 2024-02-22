# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnehot(RPackage):
	"""Fast Onehot Encoding for Data.frames

	Quickly create numeric matrices for machine learning algorithms
    that require them. It converts factor columns into onehot vectors.
	"""
	
	cran = "onehot" 

	version("0.1.1", md5="3fb8363928516f3aef06e6371de61f06")

