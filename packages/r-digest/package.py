# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDigest(RPackage):
	"""Create Compact Hash Digests of R Objects.

	Implementation of a function 'digest()' for the creation of hash digests of
	arbitrary R objects (using the md5, sha-1, sha-256, crc32, xxhash and
	murmurhash algorithms) permitting easy comparison of R language objects, as
	well as a function 'hmac()' to create hash-based message authentication
	code. The md5 algorithm by Ron Rivest is specified in RFC 1321, the sha-1
	and sha-256 algorithms are specified in FIPS-180-1 and FIPS-180-2, and the
	crc32 algorithm is described in
	ftp://ftp.rocksoft.com/cliens/rocksoft/papers/crc_v3.txt. For md5, sha-1,
	sha-256 and aes, this package uses small standalone implementations that
	were provided by Christophe Devine. For crc32, code from the zlib library
	is used. For sha-512, an implementation by Aaron D. Gifford is used. For
	xxhash, the implementation by Yann Collet is used. For murmurhash, an
	implementation by Shane Day is used. Please note that this package is not
	meant to be deployed for cryptographic purposes for which more
	comprehensive (and widely tested) libraries such as OpenSSL should be
	used."""

	cran = "digest"

	license("GPL-2.0-or-later")

	version("0.6.35", md5="5982282cd780b1202925fe8f5a06a52e")

	depends_on("r@3.3:", type=("build", "run"))
