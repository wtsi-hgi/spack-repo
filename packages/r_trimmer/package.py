# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrimmer(RPackage):
	"""Trim an Object

	A lightweight toolkit to reduce the size of a list object. The
    object is minimized by recursively removing elements from the object 
    one-by-one. The process is constrained by a reference function call
    specified by the user, where the target object is given as an argument. 
    The procedure will not allow elements to be removed from the object, that 
    will cause results from the function call to diverge from the function 
    call with the original object.
	"""
	
	cran = "trimmer" 

	version("0.8.1", md5="14e8d233ce39c0d26f024bf52ae82f0b")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
