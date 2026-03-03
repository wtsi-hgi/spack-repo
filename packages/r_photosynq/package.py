# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotosynq(RPackage):
	"""Connect to PhotosynQ

	Connect R to the PhotosynQ platform (<https://photosynq.org>). It allows to login and logout,
    as well as receive project information and project data. Further it transforms the received JSON objects
    into a data frame, which can be used for the final data analysis.
	"""
	
	homepage = "https://github.com/Photosynq/PhotosynQ-R"
	cran = "PhotosynQ" 

	version("0.2.3", md5="31a4fa3e1e49ca08e806fb6ae8c1b303")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-getpass@0.2.2:", type=("build", "run"))
