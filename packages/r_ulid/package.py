# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUlid(RPackage):
	"""Generate Universally Unique 'Lexicographically' 'Sortable'
Identifiers

	Universally unique identifiers ('UUIDs') can be sub-optimal for many
  uses-cases because they are not the most character efficient way of encoding
  128 bits of randomness; v1/v2 versions are impractical in many environments,
  as they require access to a unique, stable MAC address; v3/v5 versions require
  a unique seed and produce randomly distributed IDs, which can cause fragmentation
  in many data structures; v4 provides no other information than randomness which
  can cause fragmentation in many data structures. Providing an alternative, 'ULIDs'
  (<https://github.com/ulid/spec>) have 128-bit compatibility with 'UUID', 1.21e+24
  unique 'ULIDs' per millisecond, support standard (text) sorting, canonically encoded
  as a 26 character string, as opposed to the 36 character 'UUID', use 'base32'
  encoding for better efficiency and readability (5 bits per character), are case
  insensitive, have no special characters (i.e. are 'URL' safe) and have a monotonic
  sort order (correctly detects and handles the same millisecond).
	"""
	
	homepage = "https://github.com/eddelbuettel/ulid"
	cran = "ulid" 

	version("0.3.1", md5="2893bf019c93c8321c1ed27f6328ec4b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
