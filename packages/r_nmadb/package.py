# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmadb(RPackage):
	"""Network Meta-Analysis Database API

	Set of functions for accessing database of network meta-analyses described in 
  Petropoulou M, et al. Bibliographic study showed improving statistical methodology of network
  meta-analyses published between 1999 and 2015
  <doi:10.1016/j.jclinepi.2016.11.002>. The database is hosted in a REDcap database at the 
  Institute of Social and Preventive Medicine (ISPM) in the University of Bern.
	"""
	
	cran = "nmadb" 

	version("1.2.0", md5="9f3d448c7fffca698547775a0a82e511")

	depends_on("r@3.3.1:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
