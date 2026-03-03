# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeem(RPackage):
	"""Laboratory of Teaching to Statistics and Mathematics

	Educational tool for teaching of statistics 
    and mathematics in primary and higher education. The objective is 
    to assist in teaching/learning for both student study planning 
    and teacher teaching strategies. The 'leem' package will try to bring, 
    in a simple and at the same time in-depth, 
    knowledge of statistics and mathematics to everyone 
    who wants to study these areas of knowledge. The main function of the 
    package is 'leem()' function.
	"""
	
	homepage = "https://bendeivide.github.io/project/leem/"
	cran = "leem" 

	version("0.1.0", md5="73794ce9ee5afcb9833cd5ac2faff70c")

	depends_on("r-tkrplot", type=("build", "run"))
