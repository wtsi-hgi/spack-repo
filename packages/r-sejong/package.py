# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSejong(RPackage):
	"""KoNLP static dictionaries and Sejong project resources

	Sejong(http://www.sejong.or.kr/) corpus and
        Hannanum(http://semanticweb.kaist.ac.kr/home/index.php/HanNanum)
        dictionaries for KoNLP
	"""
	
	homepage = "https://github.com/haven-jeon/Sejong"
	cran = "Sejong" 

	version("0.01", md5="e9067fc6dab9f9563f475914389259d6")

	depends_on("r@2.14:", type=("build", "run"))
