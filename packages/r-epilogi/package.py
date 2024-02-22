# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpilogi(RPackage):
	"""The 'epilogi' Variable Selection Algorithm for Continuous Data

	The 'epilogi' variable selection algorithm is implemented for the case of continuous response and predictor variables. The relevant paper is: Lakiotaki K., Papadovasilakis Z., Lagani V., Fafalios S., Charonyktakis P., Tsagris M. and Tsamardinos I. (2023). "Automated machine learning for Genome Wide Association Studies". Bioinformatics. <doi:10.1002/sim.4780120902>. 
	"""
	
	cran = "epilogi" 

	version("1.0", md5="f92788006c8cf49ba4f9bbc14071d337")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
