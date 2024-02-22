# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTenispolar(RPackage):
	"""Provides ZENIT-POLAR Substitution Cipher Method of Encryption

	Implementation of ZENIT-POLAR substitution cipher method of encryption using by default the TENIS-POLAR cipher. This last cipher of encryption became famous through the collection of Brazilian books "Os Karas" by the author Pedro Bandeira. For more details, see "A Cryptographic Dictionary" (GC&CS, 1944). 
	"""
	
	homepage = "https://github.com/adelmofilho/tenispolaR"
	cran = "tenispolaR" 

	version("0.1.4", md5="290e8b4f814759c855a952766620f2dd")

	depends_on("r-stringr", type=("build", "run"))
