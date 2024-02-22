# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFingerprint(RPackage):
	"""Functions to Operate on Binary Fingerprint Data

	Functions to manipulate binary fingerprints
 of arbitrary length. A fingerprint is represented by an object of S4 class 'fingerprint'
 which is internally represented a vector of integers, such
 that each element represents the position in the fingerprint that is set to 1.
 The bitwise logical functions in R are overridden so that they can be used directly
 with 'fingerprint' objects. A number of distance metrics are also
 available (many contributed by Michael Fadock). Fingerprints 
 can be converted to Euclidean vectors (i.e., points on the unit hypersphere) and
 can also be folded using OR.  Arbitrary fingerprint formats can be handled via line
 handlers. Currently handlers are provided for CDK, MOE and BCI fingerprint data.
	"""
	
	cran = "fingerprint" 

	version("3.5.7", md5="9f3ce05294da928bc745ad06e562a709")

