# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDracor(RPackage):
	"""Decode Draco Format 3D Mesh Data

	Decodes meshes and point cloud data encoded by the Draco mesh
    compression library from Google. Note that this is only designed for basic
    decoding and not intended as a full scale wrapping of the Draco library.
	"""
	
	homepage = "https://github.com/natverse/dracor"
	cran = "dracor" 

	version("0.2.6", md5="d591701e7ea64631b37ac5994ff27f13")

	depends_on("r-rcpp", type=("build", "run"))
