# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecoder(RPackage):
	"""Decode Coded Variables to Plain Text and the Other Way Around

	Main function "decode" is used to decode coded key values to plain
    text. Function "code" can be used to code plain text to code if there is a
    1:1 relation between the two. The concept relies on 'keyvalue' objects used
    for translation. There are several 'keyvalue' objects included in the areas
    of geographical regional codes, administrative health care unit codes,
    diagnosis codes and more. It is also easy to extend the use by arbitrary 
    code sets.
	"""
	
	homepage = "https://www.bitbucket.com/cancercentrum/decoder"
	cran = "decoder" 

	version("1.2.2", md5="38b92f45881b6bb7b09cce6043355371")

	depends_on("r@2.10:", type=("build", "run"))
