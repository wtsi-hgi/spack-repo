# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingbook(RPackage):
	"""Survey Sampling Procedures

	Sampling procedures from the book 'Stichproben - Methoden und praktische Umsetzung mit R' by Goeran Kauermann and Helmut Kuechenhoff (2010).
	"""
	
	homepage = "https://www.samplingbook.manitz.org"
	cran = "samplingbook" 

	version("1.2.4", md5="ac486645595a901abdba5a07179b47d3")

	depends_on("r-pps", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
