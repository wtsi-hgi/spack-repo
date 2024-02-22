# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmss(RPackage):
	"""Datasets for Agresti and Finlay's "Statistical Methods for the
Social Sciences"

	Datasets used in "Statistical Methods for the Social Sciences"
    (SMSS) by Alan Agresti and Barbara Finlay.
	"""
	
	cran = "smss" 

	version("1.0-2", md5="968cd2a6b8382a90f04292073559995f")

