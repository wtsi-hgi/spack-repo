# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBbi(RPackage):
	"""Benthic Biotic Indices Calculation from Composition Data

	Set of functions to calculate Benthic Biotic Indices from
	composition data, obtained whether from morphotaxonomic inventories or
	sequencing data. Based on reference ecological weights publicly available for
	a set of commonly used marine biotic indices, such as AMBI (A Marine Biotic Index, Borja et al., 2000) <doi:10.1016/S0025-326X(00)00061-8>
	NSI (Norwegian Sensitivity Index) and ISI (Indicator Species Index) (Rygg 2013, <ISBN:978-82-577-6210-0>). It provides the ecological quality status of the samples based on each BBI as well as the normalized Ecological Quality Ratio.
	"""
	
	homepage = "https://github.com/trtcrd/BBI"
	cran = "BBI" 

	version("0.3.0", md5="2c4312dee4bbc531ff966fe6750f3da0")

	depends_on("r-vegan", type=("build", "run"))
