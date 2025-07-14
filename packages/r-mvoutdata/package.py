# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvoutdata(RPackage):
	"""affy and illumina raw data for assessing outlier detector performance

	affy and illumina raw data for assessing outlier detector performance
	"""
	
	bioc = "mvoutData"

	version("1.44.0", commit="808472247ea7887262f8fceb249b7594e165d0db")
	version("1.38.0", commit="c69f487be220b54807c16ee0b8519ab2a8aa9997")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

