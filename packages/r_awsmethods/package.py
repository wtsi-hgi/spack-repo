# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAwsmethods(RPackage):
	"""Class and Methods Definitions for Packages 'aws', 'adimpro',
'fmri', 'dwi'

	Defines the method extract and provides 'openMP' support as needed in several packages.
	"""
	
	homepage = "http://www.wias-berlin.de/software/imaging/"
	cran = "awsMethods" 

	version("1.1-1", md5="2a9265bc79c127c7a5c153bcefae6948")

	depends_on("r@3.2:", type=("build", "run"))
