# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsmartlyio(RPackage):
	"""Loading Facebook and Instagram Advertising Data from
'Smartly.io'

	Aims at loading Facebook and Instagram advertising data from
    'Smartly.io' into R. 'Smartly.io' is an online advertising service that enables
    advertisers to display commercial ads on social media networks (see <http://www.smartly.io/> for more information).
    The package offers an interface to query the 'Smartly.io' API and loads data directly into R for further data processing and data analysis.
	"""
	
	homepage = "https://github.com/rstats-lab/RSmartlyIO"
	cran = "RSmartlyIO" 

	version("0.1.3", md5="5a705453e1ae82a3ed8f7efe4e7fecc3")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
