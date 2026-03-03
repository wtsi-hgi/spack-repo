# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJiebard(RPackage):
	"""Chinese Text Segmentation Data for jiebaR Package

	jiebaR is a package for Chinese text segmentation, keyword extraction
   and speech tagging. This package provides the data files required by jiebaR.
	"""
	
	homepage = "https://github.com/qinwf/jiebaRD/"
	cran = "jiebaRD" 

	version("0.1", md5="97127d4c195f77e77d1798004ba972a0")

