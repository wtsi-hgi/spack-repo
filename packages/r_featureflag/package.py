# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeatureflag(RPackage):
	"""Turn Features On and Off using Feature Flags

	Feature flags allow developers to turn features of their
    software on and off in form of configuration. This package provides
    functions for creating feature flags in code. It exposes an interface
    for defining own feature flags which are enabled based on custom criteria.
	"""
	
	homepage = "https://github.com/szymanskir/featureflag"
	cran = "featureflag" 

	version("0.1.0", md5="6203fc49f9175f8353e656fbc1cb3e65")

