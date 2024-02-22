# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdatools(RPackage):
	"""Multivariate Data Analysis for Chemometrics

	Projection based methods for preprocessing, exploring and analysis of multivariate data used in chemometrics. S. Kucheryavskiy (2020) <doi:10.1016/j.chemolab.2020.103937>.
	"""
	
	homepage = "https://mda.tools"
	cran = "mdatools" 

	version("0.14.1", md5="261884057996cc4e5e166b6c909d644d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
