# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrimate(RPackage):
	"""Tools and Methods for Primatological Data Science

	Data from All the World's Primates relational SQL database and other tabular datasets are made available via drivers and connection functions. Additionally we provide several functions and examples to facilitate the merging and aggregation of these tabular inputs. 
	"""
	
	cran = "primate" 

	version("0.2.0", md5="2c53744cbc7be7c17065f21971c2a1d9")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-caroline", type=("build", "run"))
