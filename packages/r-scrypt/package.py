# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrypt(RPackage):
	"""Key Derivation Functions for R Based on Scrypt

	Functions for working with the scrypt key derivation functions
    originally described by Colin Percival
    <https://www.tarsnap.com/scrypt/scrypt.pdf> and in Percival and Josefsson
    (2016) <doi:10.17487/RFC7914>. Scrypt is a password-based key derivation
    function created by Colin Percival. The algorithm was specifically designed
    to make it costly to perform large-scale custom hardware attacks by
    requiring large amounts of memory.
	"""
	
	homepage = "https://github.com/bobjansen/rscrypt"
	cran = "scrypt" 

	version("0.1.6", md5="c3a4b02d972f92d056cdfe561c9a4b01")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
