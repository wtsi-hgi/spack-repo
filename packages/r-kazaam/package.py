# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKazaam(RPackage):
	"""Tools for Tall Distributed Matrices

	Many data science problems reduce to operations on very tall,
    skinny matrices.  However, sometimes these matrices can be so tall that they
    are difficult to work with, or do not even fit into main memory.  One
    strategy to deal with such objects is to distribute their rows across
    several processors.  To this end, we offer an 'S4' class for tall, skinny,
    distributed matrices, called the 'shaq'.  We also provide many useful
    numerical methods and statistics operations for operating on these
    distributed objects.  The naming is a bit "tongue-in-cheek", with the class
    a play on the fact that 'Shaquille' 'ONeal' ('Shaq') is very tall, and he
    starred in the film 'Kazaam'.
	"""
	
	homepage = "http://r-pbd.org/"
	cran = "kazaam" 

	version("0.1-0", md5="5a2c2438a88ce72266ce60acdb0ced13")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pbdmpi@0.3.0:", type=("build", "run"))
