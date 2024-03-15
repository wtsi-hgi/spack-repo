# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHce(RPackage):
	"""Design and Analysis of Hierarchical Composite Endpoints

	Simulate and analyze hierarchical composite endpoints. Win odds is the main analysis method, but other win statistics (win ratio, net benefit) are implemented as well in case of no censoring. See Gasparyan SB et al (2023) "Hierarchical Composite Endpoints in COVID-19: The DARE-19 Trial." Case Studies in Innovative Clinical Trials, 95-148. Chapman; Hall/CRC. <doi:10.1201/9781003288640-7>.
	"""
	
	cran = "hce" 

	version("0.6.0", md5="27040c32ea4e4f8e668a582750ddc4b5")

	depends_on("r@2.10:", type=("build", "run"))
