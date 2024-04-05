# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisachartr(RPackage):
	"""Wrapper for 'Visa Chart Components'

	Provides a set of wrapper functions for 'Visa Chart Components'.
  'Visa Chart Components' <https://github.com/visa/visa-chart-components> is an accessibility focused,
  framework agnostic set of data experience design systems components for the web.
	"""
	
	homepage = "https://github.com/visa/visa-chart-components/tree/master/packages/charts-R"
	cran = "visachartR" 

	version("3.3.0", md5="c60b0a434099eefe16b4e20501c10c09")
	version("3.2.0", md5="a2281eac1cc678215b55d4e14f8e8f3d")

	depends_on("r-htmlwidgets", type=("build", "run"))
