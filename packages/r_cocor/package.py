# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCocor(RPackage):
	"""Comparing Correlations

	Statistical tests for the comparison between two correlations based on either independent or dependent groups. Dependent correlations can either be overlapping or nonoverlapping. A web interface is available on the website <http://comparingcorrelations.org>. A plugin for the R GUI and IDE RKWard is included. Please install RKWard from <https://rkward.kde.org> to use this feature. The respective R package 'rkward' cannot be installed directly from a repository, as it is a part of RKWard.
	"""
	
	homepage = "http://comparingcorrelations.org"
	cran = "cocor" 

	version("1.1-4", md5="2e5d0b5a82bd9db4d0d1b33201c0f481")

