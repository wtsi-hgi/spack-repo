# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecretbase(RPackage):
	"""Cryptographic Hash and Extendable-Output Functions

	SHA-256, SHA-3 cryptographic hash and SHAKE256 extendable-output
    functions (XOF). The SHA-3 Secure Hash Standard was published by the
    National Institute of Standards and Technology (NIST) in 2015 at
    <doi:10.6028/NIST.FIPS.202>. The SHA-256 Secure Hash Standard was published
    by NIST in 2002 at
    <https://csrc.nist.gov/publications/fips/fips180-2/fips180-2.pdf>. Fast and
    memory-efficient implementation using the core algorithms from 'Mbed TLS'
    under the Trusted Firmware Project
    <https://www.trustedfirmware.org/projects/mbed-tls/>.
	"""
	
	homepage = "https://shikokuchuo.net/secretbase/"
	cran = "secretbase" 

	version("0.3.0.1", md5="e6f9c238f463c7b4f850e18988167972")
	version("0.3.0", md5="87d9c1c967bcbdcdf4c6db3541bc905d")

	depends_on("r@3.5:", type=("build", "run"))
