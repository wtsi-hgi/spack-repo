# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChineseMisc(RPackage):
	"""Miscellaneous Tools for Chinese Text Mining and More

	Efforts are made to make Chinese text mining easier, faster, and robust to errors. 
    Document term matrix can be generated by only one line of code; detecting encoding, 
    segmenting and removing stop words are done automatically. 
	Some convenient tools are also supplied.
	"""
	
	homepage = "https://github.com/githubwwwjjj/chinese.misc/blob/master/README.md"
	cran = "chinese.misc" 

	version("0.2.3", md5="72c4829486a6b97f1ba2059ec5137f68")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jiebar", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-tm@0.7:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-slam@0.1.37:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
