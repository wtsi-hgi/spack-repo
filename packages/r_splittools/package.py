# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplittools(RPackage):
	"""Tools for Data Splitting

	Fast, lightweight toolkit for data splitting. Data sets can
    be partitioned into disjoint groups (e.g. into training, validation,
    and test) or into (repeated) k-folds for subsequent cross-validation.
    Besides basic splits, the package supports stratified, grouped as well
    as blocked splitting. Furthermore, cross-validation folds for time
    series data can be created. See e.g. Hastie et al. (2001)
    <doi:10.1007/978-0-387-84858-7> for the basic background on data
    partitioning and cross-validation.
	"""
	
	homepage = "https://github.com/mayer79/splitTools"
	cran = "splitTools" 

	version("1.0.1", md5="04d4df261072a42390d8ff002b21f071")

