# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForwards(RPackage):
	"""Data from Surveys Conducted by Forwards

	Anonymized data from surveys conducted by Forwards <https://forwards.github.io/>, the R Foundation task force on women and other under-represented groups. Currently, a single data set of responses to a survey of attendees at useR! 2016 <https://www.r-project.org/useR-2016/>, the R user conference held at Stanford University, Stanford, California, USA, June 27 - June 30 2016.
	"""
	
	homepage = "https://github.com/forwards/forwards"
	cran = "forwards" 

	version("0.1.3", md5="5483aa3861178b9a1876bfbbcff870c4")

	depends_on("r@2.10:", type=("build", "run"))
