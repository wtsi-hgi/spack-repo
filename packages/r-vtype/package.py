# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVtype(RPackage):
	"""Estimates the Variable Type in Error Afflicted Data

	Estimates the type of variables in non-quality controlled data. The prediction is based on a random forest model, trained on over 5000 medical variables with accuracy of 99%. The accuracy can hardy depend on type and coding style of data.
	"""
	
	cran = "vtype" 

	version("0.8", md5="c701162e8edd942bcc693c7cfa79cf78")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
