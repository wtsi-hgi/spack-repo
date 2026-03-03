# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocalcr(RPackage):
	"""Isotope Calculations in R

	Perform common calculations based on published stable isotope theory, such as calculating carbon isotope discrimination and intrinsic water use efficiency from wood or leaf carbon isotope composition. See Mathias and Hudiburg (2022) in Global Change Biology <doi:10.1111/gcb.16407>.  
	"""
	
	homepage = "https://github.com/justinmathias/isocalcR"
	cran = "isocalcR" 

	version("0.1.1", md5="410579338e3882d480f2fa2b82c3f8c7")

	depends_on("r@4:", type=("build", "run"))
