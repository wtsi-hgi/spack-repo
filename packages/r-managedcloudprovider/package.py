# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManagedcloudprovider(RPackage):
	"""Providing the Kubernetes-Like Functions for the Non-Kubernetes
Cloud Service

	
  Providing the kubernetes-like class 'ManagedCloudProvider' as a child class of 
  the 'CloudProvider' class in the 'DockerParallel' package. The class is able to
  manage the cloud instance made by the non-kubernetes cloud service.
  For creating a provider for the non-kubernetes cloud service, the developer
  needs to define a reference class inherited from 'ManagedCloudProvider' and
  define the method for the generics runDockerWorkerContainers(),
  getDockerWorkerStatus() and killDockerWorkerContainers(). For more information, please see
  the vignette in this package and <https://CRAN.R-project.org/package=DockerParallel>.
	"""
	
	homepage = "https://github.com/Jiefei-Wang/ManagedCloudProvider"
	cran = "ManagedCloudProvider" 

	version("1.0.0", md5="522179a01a3da2d50e2472dc45f98043")

	depends_on("r-dockerparallel@1.0.3:", type=("build", "run"))
	depends_on("r-adagio", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
