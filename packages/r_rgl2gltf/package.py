# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgl2gltf(RPackage):
	"""Read and Write '.gltf' and '.glb' Files

	The 'glTF' file format is used to describe 3D models.  This package 
 provides read and write functions to work with it.
	"""
	
	homepage = "https://github.com/dmurdoch/rgl2gltf"
	cran = "rgl2gltf" 

	version("1.0.3", md5="bd7807559099c30882a4cbe328c901d9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rgl@0.108.43:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
