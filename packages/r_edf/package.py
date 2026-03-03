# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REdf(RPackage):
	"""Read Data from European Data Format (EDF and EDF+) Files

	Import physiologic data stored in
    the European Data Format (EDF and EDF+) into R.
    Both EDF and EDF+ files are supported. Discontinuous
    EDF+ files are not yet supported.
	"""
	
	homepage = "https://github.com/bwrc/edf"
	cran = "edf" 

	version("1.0.0", md5="0bca2b2a205ab3433b4d0a7b05c6c56f")

	depends_on("r@3.0.2:", type=("build", "run"))
