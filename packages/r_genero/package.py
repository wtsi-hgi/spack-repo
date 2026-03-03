# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenero(RPackage):
	"""Estimate Gender from Names in Spanish and Portuguese

	Estimate gender from names in Spanish and Portuguese. 
    Works with vectors and dataframes. The estimation works not only
    for first names but also full names. The package relies on a
    compilation of common names with it's most frequent associated 
    gender in both languages which are used as look up tables for gender
    inference.
	"""
	
	homepage = "https://github.com/datasketch/genero"
	cran = "genero" 

	version("0.1.0", md5="1893452d9983008c69779b1a8af176dc")

	depends_on("r@3.1:", type=("build", "run"))
