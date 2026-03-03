# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHashr(RPackage):
	"""Hash R Objects to Integers Fast

	Apply an adaptation of the SuperFastHash algorithm to any R
    object. Hash whole R objects or, for vectors or lists, hash R objects to obtain
    a set of hash values that is stored in a structure equivalent to the input. See
    <http://www.azillionmonkeys.com/qed/hash.html> for a description of the hash
    algorithm.
	"""
	
	homepage = "https://github.com/markvanderloo/hashr"
	cran = "hashr" 

	version("0.1.4", md5="c5346006b727f164d719e0ddf2c30088")

