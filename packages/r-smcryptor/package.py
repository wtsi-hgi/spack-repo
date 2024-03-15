# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmcryptor(RPackage):
	"""ShangMi(SM) Cryptographic Algorithms(SM2/SM3/SM4)

	Bindings to 'smcrypto' <https://github.com/zhuobie/smcrypto>: a 'Rust'
    implementation of China's Standards of Encryption Algorithms, which is usually 
    called 'ShangMi(SM)' algorithms. It contains 'SM3' message digest algorithm, 
    'SM2' asymmetric encryption algorithm and 'SM4' symmetric encryption algorithm. 
    Users can do message hash, encrypt/decrypt, sign/verify, key exchange and more.
	"""
	
	homepage = "https://github.com/zhuobie/smcryptoR"
	cran = "smcryptoR" 

	version("0.1.1", md5="96403224d84981dbb69b79d4fa5fe8f8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
