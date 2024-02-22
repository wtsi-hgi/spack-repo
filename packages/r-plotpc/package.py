# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotpc(RPackage):
	"""Plot Principal Component Histograms Around a Scatter Plot

	Plot principal component histograms around a bivariate
        scatter plot.
	"""
	
	homepage = "http://www.milbo.users.sonic.net"
	cran = "plotpc" 

	version("1.0.4", md5="4eded1a9022c0cdbc69984dae1f35f96")

