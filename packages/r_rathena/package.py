# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRathena(RPackage):
	"""Connect to 'AWS Athena' using 'Boto3' ('DBI' Interface)

	Designed to be compatible with the R package 'DBI' (Database Interface)
    when connecting to Amazon Web Service ('AWS') Athena <https://aws.amazon.com/athena/>.
    To do this 'Python' 'Boto3' Software Development Kit ('SDK')
    <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html> is used as a driver.
	"""
	
	homepage = "https://github.com/DyfanJones/RAthena"
	cran = "RAthena" 

	version("2.6.1", md5="5d3c6d5e2c1a0ca96d4dfa69b9231fa6")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-dbi@0.7:", type=("build", "run"))
	depends_on("r-reticulate@1.13:", type=("build", "run"))
	depends_on("r-uuid@0.1.4:", type=("build", "run"))
