# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocron(RPackage):
	"""Statistical Comparisons of Two or more Alpha Coefficients

	Statistical tests for the comparison between two or more alpha
    coefficients based on either dependent or independent groups of individuals.
    A web interface is available at http://comparingcronbachalphas.org. A plugin
    for the R GUI and IDE RKWard is included. Please install RKWard from https://
    rkward.kde.org to use this feature. The respective R package 'rkward' cannot be
    installed directly from a repository, as it is a part of RKWard.
	"""
	
	homepage = "http://comparingcronbachalphas.org"
	cran = "cocron" 

	version("1.0-1", md5="035ec48950403bb242c36e59d995eaa0")

