# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoctua(RPackage):
	"""Connect to 'AWS Athena' using R 'AWS SDK' 'paws' ('DBI'
Interface)

	Designed to be compatible with the 'R' package 'DBI' (Database Interface)
    when connecting to Amazon Web Service ('AWS') Athena <https://aws.amazon.com/athena/>.
    To do this the 'R' 'AWS' Software Development Kit ('SDK') 'paws' 
    <https://github.com/paws-r/paws> is used as a driver.
	"""
	
	homepage = "https://github.com/DyfanJones/noctua"
	cran = "noctua" 

	version("2.6.2", md5="b586b39fd735788ffa34caf10b8f2216")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-dbi@0.7:", type=("build", "run"))
	depends_on("r-paws@0.2:", type=("build", "run"))
	depends_on("r-uuid@0.1.4:", type=("build", "run"))
