# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGender(RPackage):
	"""Predict Gender from Names Using Historical Data

	Infers state-recorded gender categories from first names and dates of birth using historical
    datasets. By using these datasets instead of lists of male and female names,
    this package is able to more accurately infer the gender of a name, and it
    is able to report the probability that a name was male or female. GUIDELINES:
    This method must be used cautiously and responsibly. Please be sure to see the
    guidelines and warnings about usage in the 'README' or the package documentation.
    See Blevins and Mullen (2015) <http://www.digitalhumanities.org/dhq/vol/9/3/000223/000223.html>.
	"""
	
	homepage = "https://github.com/lmullen/gender"
	cran = "gender" 

	version("0.6.0", md5="7bb022a5470ac85e6474d036a9c43f0b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.6.1:", type=("build", "run"))
	depends_on("r-remotes@2.2:", type=("build", "run"))
