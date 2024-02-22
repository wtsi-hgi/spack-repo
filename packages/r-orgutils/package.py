# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrgutils(RPackage):
	"""Helper Functions for Org Files

	Helper functions for Org files (<https://orgmode.org/>):
  a generic function 'toOrg' for transforming R objects into Org
  markup (most useful for data frames; there are also methods for
  Dates/POSIXt) and a function to read Org tables into data frames.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/orgutils/"
	cran = "orgutils" 

	version("0.5-0", md5="0a55ada88697e175c2cc9ab630fe4fa2")

	depends_on("r-textutils", type=("build", "run"))
