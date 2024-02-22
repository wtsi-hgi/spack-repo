# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDockerparallel(RPackage):
	"""Using the Docker Container to Create R Workers on Local or Cloud
Platform

	This is the core package that provides both the user API and developer API to deploy 
    the parallel cluster on the cloud using the container service. The user can call 
    clusterPreset() to define the cloud service provider and container and makeDockerCluster()
    to create the cluster. The developer should see "developer's cookbook" on how to define
    the cloud provider and container.
	"""
	
	homepage = "https://github.com/Jiefei-Wang/DockerParallel"
	cran = "DockerParallel" 

	version("1.0.4", md5="45104218ca06cce38ce37a266d50bf1d")

	depends_on("r-jsonlite", type=("build", "run"))
