# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarsel(RPackage):
	"""Sequential Forward Floating Selection using Jeffries-Matusita
Distance

	Feature selection using Sequential Forward Floating feature Selection and Jeffries-Matusita distance. It returns a suboptimal set of features to use for image classification. Reference: Dalponte, M., Oerka, H.O., Gobakken, T., Gianelle, D. & Naesset, E. (2013). Tree Species Classification in Boreal Forests With Hyperspectral Data. IEEE Transactions on Geoscience and Remote Sensing, 51, 2632-2645, <DOI:10.1109/TGRS.2012.2216272>.
	"""
	
	cran = "varSel" 

	version("0.2", md5="de09b4e37ba93dd88e66f88e690871f8")

