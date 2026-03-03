# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROshka(RPackage):
	"""Recursive Quoted Language Expansion

	Expands quoted language by recursively replacing any symbol that
    points to quoted language with the language it points to.  The recursive
    process continues until only symbols that point to non-language objects
    remain.  The resulting quoted language can then be evaluated normally.  This
    differs from the traditional 'quote'/'eval' pattern because it resolves
    intermediate language objects that would interfere with evaluation.
	"""
	
	homepage = "https://github.com/brodieG/oshka"
	cran = "oshka" 

	version("0.1.2", md5="b71cc00b9fe96794388a75553424611c")

	depends_on("r@3.3.2:", type=("build", "run"))
