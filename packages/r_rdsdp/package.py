# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdsdp(RPackage):
	"""R Interface to DSDP Semidefinite Programming Library

	R interface to DSDP semidefinite programming library. The DSDP software is a free open source implementation of an interior-point method for semidefinite programming. It provides primal and dual solutions, exploits low-rank structure and sparsity in the data, and has relatively low memory requirements for an interior-point method. 
	"""
	
	homepage = "https://www.mcs.anl.gov/hs/software/DSDP"
	cran = "Rdsdp" 

	version("1.0.5.2.1", md5="8581d00fdac2783eaa6226b3de1171d7")

