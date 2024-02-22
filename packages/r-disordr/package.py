# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDisordr(RPackage):
	"""Non-Ordered Vectors

	Functionality for manipulating values of associative
  maps.  The package is designed to be used with the 'mvp' class of
  packages that use the STL map class: its purpose is to trap
  plausible idiom that is ill-defined (implementation-specific) and
  return an informative error, rather than returning a possibly
  incorrect result.  To cite the package in publications please use
  Hankin (2022) <doi:10.48550/ARXIV.2210.03856>.
	"""
	
	homepage = "https://github.com/RobinHankin/disordR"
	cran = "disordR" 

	version("0.9-8.2", md5="981fe4e9486273026750173a52ab3896")

	depends_on("r-matrix@1.3.3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
