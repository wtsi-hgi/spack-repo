# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoiModelsGlobalopttests(RPackage):
	"""'ROI' Optimization Problems Based on 'globalOptTests'

	A collection of non-linear optimization problems with box bounds
             transformed into 'ROI' optimization problems.
             This package provides a wrapper around the 'globalOptTests'
             which provides a collection of global optimization problems.
             More information can be found in the 'README' file.
	"""
	
	cran = "ROI.models.globalOptTests" 

	version("1.1-1", md5="319cb5fd477c8506a480fa03e3f70877")

	depends_on("r-roi@0.3.0:", type=("build", "run"))
	depends_on("r-globalopttests", type=("build", "run"))
