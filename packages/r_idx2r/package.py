# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdx2r(RPackage):
	"""Convert Files to and from IDX Format to Vectors, Matrices and
Arrays

	Convert files to and from IDX format to vectors, matrices and arrays.
    IDX is a very simple file format designed for storing vectors and multidimensional matrices in
    binary format. The format is described on the website from Yann LeCun
    <http://yann.lecun.com/exdb/mnist/>. 
	"""
	
	homepage = "https://github.com/edoffagne/idx2r"
	cran = "idx2r" 

	version("1.0.0", md5="f39977ae433878ae3539ee66bc3916e8")

