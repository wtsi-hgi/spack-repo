# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbe(RPackage):
	"""Augmented Backward Elimination

	Performs augmented backward elimination and checks the stability of the obtained model. Augmented backward elimination combines significance or information based criteria with the change in estimate to either select the optimal model for prediction purposes or to serve as a tool to obtain a practically sound, highly interpretable model. More details can be found in Dunkler et al. (2014) <doi:10.1371/journal.pone.0113677>. 
	"""
	
	cran = "abe" 

	version("3.0.1", md5="9c151db5397422c8927dee41dabfbfab")

