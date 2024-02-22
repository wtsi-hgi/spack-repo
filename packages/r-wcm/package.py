# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcm(RPackage):
	"""Water Cloud Model (WCM) for the Simulation of Leaf Area Index
(LAI) and Soil Moisture (SM) from Microwave Backscattering

	Retrieval the leaf area index (LAI) and soil moisture (SM) from  microwave backscattering data using water cloud model (WCM) model . The WCM algorithm attributed to Pervot et al.(1993) <doi:10.1016/0034-4257(93)90053-Z>. The authors are grateful to SAC, ISRO, Ahmedabad for providing financial support to Dr. Prashant K Srivastava to conduct this research work.
	"""
	
	cran = "WCM" 

	version("0.2.2", md5="7d06213430c155739f98e4e87f21c4bd")

	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
