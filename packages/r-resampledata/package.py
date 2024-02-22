# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResampledata(RPackage):
	"""Data Sets for Mathematical Statistics with Resampling in R

	Package of data sets from "Mathematical Statistics
    with Resampling in R" (1st Ed. 2011, 2nd Ed. 2018) by Laura Chihara and Tim Hesterberg.
	"""
	
	homepage = "https://github.com/rudeboybert/resampledata"
	cran = "resampledata" 

	version("0.3.1", md5="11b6f1ee83f02ea6fea6e85e86c07193")

	depends_on("r@2.10:", type=("build", "run"))
