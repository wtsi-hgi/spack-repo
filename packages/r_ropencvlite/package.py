# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopencvlite(RPackage):
	"""Helper Package for Installing OpenCV with R

	Installs 'OpenCV' for use by other packages. 'OpenCV' <https://opencv.org/> 
    is library of programming functions mainly aimed at real-time computer 
    vision. This 'Lite' version installs the stable base version of 'OpenCV' and 
    some of its experimental externally contributed modules. It does not provide 
    R bindings directly. 
	"""
	
	homepage = "https://swarm-lab.github.io/ROpenCVLite/"
	cran = "ROpenCVLite" 

	version("4.90.1", md5="9fb3fa540c341f2ca90a938242362044")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("cmake", type=("build", "link", "run"))
