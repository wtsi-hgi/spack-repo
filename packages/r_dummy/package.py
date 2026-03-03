# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDummy(RPackage):
	"""Automatic Creation of Dummies with Support for Predictive
Modeling

	Efficiently create dummies of all factors and character vectors in a data frame. Support is included for learning the categories on one data set (e.g., a training set) and deploying them on another (e.g., a test set).
	"""
	
	cran = "dummy" 

	version("0.1.3", md5="068e9b6c4f6ea40d7d92206b0a8a2a51")

