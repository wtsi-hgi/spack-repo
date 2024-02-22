# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCipher(RPackage):
	"""Encryption and Decryption with Text Ciphers

	Encrypts and decrypts using basic ciphers. None of 
  these should be used in place of real encryption using state of the art tools. 
  The ciphers included use methods described in the ciphers's Wikipedia and 
  cryptography hobby websites.
	"""
	
	cran = "cipheR" 

	version("1.0.0", md5="e770b699e74385a8c037ffe7253324a4")

