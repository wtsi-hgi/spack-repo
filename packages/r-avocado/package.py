# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvocado(RPackage):
	"""Weekly Hass Avocado Sales Summary

	Provides a weekly summary of Hass Avocado sales for the 
    contiguous US from January 2017 to November 2020. 
    See the package website for more information, documentation,
    and examples. Data source: Haas Avocado Board 
    <https://hassavocadoboard.com/category-data/>.
	"""
	
	cran = "avocado" 

	version("0.1.0", md5="6e5fc83a41fe55a16cce44989f42ac51")

	depends_on("r@2.10:", type=("build", "run"))
