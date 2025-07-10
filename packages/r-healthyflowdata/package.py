# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyflowdata(RPackage):
	"""Healthy dataset used by the flowMatch package

	A healthy dataset with 20 flow cytometry samples used by the flowMatch package.
	"""
	
	bioc = "healthyFlowData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/healthyFlowData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/healthyFlowData/healthyFlowData_1.40.0.tar.gz"]

	version("1.40.0", sha256="9d4f6673ac1ab45c414a31bafa1c56afc37e4bf9502043a3253fda89ea7826f1")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))

