# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaff(RPackage):
	"""Diff, Patch and Merge for Data.frames

	Diff, patch and merge for data frames. Document changes in data
    sets and use them to apply patches. Changes to data can be made visible by using
    render_diff(). The 'V8' package is used to wrap the 'daff.js' 'JavaScript' library
    which is included in the package.
	"""
	
	homepage = "https://github.com/edwindj/daff"
	cran = "daff" 

	version("1.1.1", md5="f243c169315e2c1bc261d8e25c726ce6")

	depends_on("r-v8@0.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
