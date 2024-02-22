# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAssocind(RPackage):
	"""Implements New and Existing Association Indices for Constructing
Animal Social Networks

	Implements several new association indices that can control for various types of errors. Also includes existing association indices and functions for simulating the effects of different rates of error on estimates of association strength between individuals using each method.
	"""
	
	cran = "assocInd" 

	version("1.0.1", md5="6432a0aecc1f1527d5d815ff03934424")

	depends_on("r@2.10:", type=("build", "run"))
