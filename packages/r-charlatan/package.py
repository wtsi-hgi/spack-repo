# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCharlatan(RPackage):
	"""Make Fake Data

	Make fake data, supporting addresses, person names, dates,
    times, colors, coordinates, currencies, digital object identifiers
    ('DOIs'), jobs, phone numbers, 'DNA' sequences, doubles and integers
    from distributions and within a range.
	"""
	
	homepage = "https://docs.ropensci.org/charlatan/"
	cran = "charlatan" 

	version("0.5.1", md5="23ee9526a9128841ef3abc767c393658")

	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-tibble@1.2:", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
