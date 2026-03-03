# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCloudutil(RPackage):
	"""Cloud Utilization Plots

	Provides means of plots for comparing utilization data of compute systems.
	"""
	
	homepage = "https://cran.r-project.org/package=cloudUtil"
	cran = "cloudUtil" 

	version("0.1.12", md5="b954ca37a97b7295f2176b7a3d6361aa")

	depends_on("r@2.11:", type=("build", "run"))
