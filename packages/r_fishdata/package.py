# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFishdata(RPackage):
	"""A Small Collection of Fish Population Datasets

	A collection of four datasets 
    based around the population dynamics of migratory fish. Datasets 
    contain both basic size information on a per fish basis, as well as
    otolith data that contains a per day record of fish growth history.
    All data in this package was collected by the author, from 
    2015-2016, in the Wellington region of New Zealand. 
	"""
	
	cran = "fishdata" 

	version("1.0.1", md5="846ec3868596d3d4bf62ac2f47fa64a0")

	depends_on("r@2.10:", type=("build", "run"))
