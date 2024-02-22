# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHashids(RPackage):
	"""Generate Short Unique YouTube-Like IDs (Hashes) from Integers

	An R port of the hashids library.  hashids generates YouTube-like hashes from integers or vector of integers.  Hashes generated from integers are relatively short, unique and non-seqential.  hashids can be used to generate unique ids for URLs and hide database row numbers from the user.  By default hashids will avoid generating common English cursewords by preventing certain letters being next to each other.  hashids are not one-way: it is easy to encode an integer to a hashid and decode a hashid back into an integer.
	"""
	
	homepage = "https://github.com/ALShum/hashids-r/"
	cran = "hashids" 

	version("0.9.0", md5="a11f3b23b0fbc242b3602739866f8502")

	depends_on("r@3.2.2:", type=("build", "run"))
