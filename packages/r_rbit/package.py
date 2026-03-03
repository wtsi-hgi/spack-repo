# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbit(RPackage):
	"""Binary Indexed Tree

	A simple implementation of Binary Indexed Tree by R. The BinaryIndexedTree class supports construction of Binary Indexed Tree from a vector, update of a value in the vector and query for the sum of a interval of the vector.
	"""
	
	cran = "rbit" 

	version("1.0.0", md5="71fb1134d2c416923caf3a3d86af4acb")

	depends_on("r-r6", type=("build", "run"))
