# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTclust(RPackage):
	"""Robust Trimmed Clustering.

	Provides functions for robust trimmed clustering. The methods are described
	in Garcia-Escudero (2008) <doi:10.1214/07-AOS515>, Fritz et al. (2012)
	<doi:10.18637/jss.v047.i12>, Garcia-Escudero et al. (2011)
	<doi:10.1007/s11222-010-9194-z> and others."""

	cran = "tclust"

	version("1.5-6", md5="d4078d45e8cd522cf3bfff08d9ec04ee")

	depends_on("r@3.6.2:", type=("build", "run"))
