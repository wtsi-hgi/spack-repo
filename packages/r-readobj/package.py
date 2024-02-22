# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadobj(RPackage):
	"""Fast Reader for 'Wavefront' OBJ 3D Scene Files

	Wraps 'tiny_obj_loader' C++ library for reading the 'Wavefront' OBJ
    3D file format including both mesh objects and materials files. The
    resultant R objects are either structured to match the 'tiny_obj_loader'
    internal data representation or in a form directly compatible with the 'rgl'
    package.
	"""
	
	homepage = "https://github.com/jefferis/readobj"
	cran = "readobj" 

	version("0.4.1", md5="cd885dfa4fa4bc43997f65f6520085e1")

	depends_on("r-rcpp", type=("build", "run"))
