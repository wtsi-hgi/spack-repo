# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcereal(RPackage):
	"""C++11 Header Files for 'cereal'

	To facilitate using 'cereal' with Rcpp.
    'cereal' is a header-only C++11 serialization library.
    'cereal' takes arbitrary data types and reversibly turns them into
    different representations, such as compact binary encodings, XML,
    or JSON. 'cereal' was designed to be fast, light-weight, and easy
    to extend - it has no external dependencies and can be easily
    bundled with other code or used standalone. Please see
    <http://uscilab.github.io/cereal> for more information.
	"""
	
	homepage = "https://github.com/wush978/Rcereal"
	cran = "Rcereal" 

	version("1.2.1.1", md5="25570096366882d600c24fb9e656661a")

