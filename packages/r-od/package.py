# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROd(RPackage):
	"""Manipulate and Map Origin-Destination Data

	The aim of 'od' is to provide tools and example datasets for working with
  origin-destination ('OD') datasets of the type used to describe aggregate
  urban mobility patterns (Carey et al. 1981) <doi:10.1287/trsc.15.1.32>.
  The package builds on functions for working with 'OD' data in the package 'stplanr',
  (Lovelace and Ellison 2018) <doi:10.32614/RJ-2018-053> with a focus on computational
  efficiency and support for  the 'sf' class system (Pebesma 2018) <doi:10.32614/RJ-2018-009>.
  With few dependencies and a simple class system based on data frames,
  the package is intended to facilitate efficient analysis of 'OD' datasets
  and to provide a place for developing new functions.
  The package enables the creation and analysis of geographic entities
  representing large scale mobility patterns,
  from daily travel between zones in cities to migration between countries.
	"""
	
	homepage = "https://github.com/itsleeds/od"
	cran = "od" 

	version("0.4.3", md5="070020d778a099d47238f3763197df19")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sfheaders", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
