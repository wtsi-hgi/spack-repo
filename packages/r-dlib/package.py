# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlib(RPackage):
	"""Allow Access to the 'Dlib' C++ Library

	Interface for 'Rcpp' users to 'dlib' <http://dlib.net> which is a
    'C++' toolkit containing machine learning algorithms and computer vision tools.
    It is used in a wide range of domains including robotics, embedded devices,
    mobile phones, and large high performance computing environments. This package
    allows R users to use 'dlib' through 'Rcpp'.
	"""
	
	cran = "dlib" 

	version("1.0.3.1", md5="c31a2e5b9aed062b4fbce736329b67d0")

	depends_on("r-rcpp", type=("build", "run"))
