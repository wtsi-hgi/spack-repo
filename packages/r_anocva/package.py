# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnocva(RPackage):
	"""A Non-Parametric Statistical Test to Compare Clustering
Structures

	Provides ANOCVA (ANalysis Of Cluster VAriability), a non-parametric statistical test
    to compare clustering structures with applications in functional magnetic resonance imaging
    data (fMRI). The ANOCVA allows us to compare the clustering structure of multiple groups
    simultaneously and also to identify features that contribute to the differential clustering.
	"""
	
	cran = "anocva" 

	version("0.1.1", md5="f217a9c2c22909f0d4111c767c3ef929")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
