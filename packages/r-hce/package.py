# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHce(RPackage):
	"""Design and Analysis of Hierarchical Composite Endpoints

	Simulate and analyze hierarchical composite endpoints. Win odds is the main analysis method. See Gasparyan SB et al (2022) "Design and Analysis of Studies Based on Hierarchical Composite Endpoints: Insights from the DARE-19 Trial." Therapeutic Innovation & Regulatory Science 56: 785–794. <doi:10.1007/s43441-022-00420-1>.
	"""
	
	cran = "hce" 

	version("0.5.9", md5="74bbfcb70382d293cf0e27c77a3ce197")

	depends_on("r@2.10:", type=("build", "run"))
