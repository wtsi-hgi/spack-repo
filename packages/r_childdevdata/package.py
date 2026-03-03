# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChilddevdata(RPackage):
	"""Child Development Data

	Measuring child development starts by collecting responses to 
    developmental milestones, such as "able to sit" or "says two words". 
    There are many ways to combine such responses into summaries. 
    The package bundles publicly available datasets with individual milestone 
    data for children aged 0-5 years, with the aim of supporting the construction, 
    evaluation, validation and interpretation of methodologies that aggregate 
    milestone data into informative measures of child development.
	"""
	
	homepage = "https://github.com/d-score/childdevdata"
	cran = "childdevdata" 

	version("1.1.0", md5="365531edfe5973ec5441565179926df5")

	depends_on("r@2.10:", type=("build", "run"))
