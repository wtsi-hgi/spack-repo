# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowfp(RPackage):
	"""Fingerprinting for Flow Cytometry

	Fingerprint generation of flow cytometry data, used to facilitate the application of machine learning and datamining tools for flow cytometry.
	"""
	
	bioc = "flowFP"

	version("1.66.0", commit="5cf0089efd7f7f74beede54c9a75914156c1d787")
	version("1.60.0", commit="5e8bb56cdbc185070480e1009b09671325294db3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-flowviz", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics@0.1.6:", type=("build", "run"))
