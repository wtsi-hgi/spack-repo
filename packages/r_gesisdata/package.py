# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGesisdata(RPackage):
	"""Reproducible Data Retrieval from the GESIS Data Archive

	Reproducible, programmatic retrieval of datasets from the
    GESIS Data Archive.  The GESIS Data Archive <https://search.gesis.org>  
    makes available thousands of invaluable datasets, but researchers using
    these datasets are caught in a bind.  The archive's terms and conditions
    bar dissemination of downloaded datasets to third parties, but to ensure 
    that one's work can be reproduced, assessed, and built upon by others, one
    must provide access to the raw data one has employed.  The 'gesisdata'
    package cuts this knot by providing registered users with programmatic,
    reproducible access to GESIS datasets from within 'R'.
	"""
	
	homepage = "https://github.com/fsolt/gesisdata"
	cran = "gesisdata" 

	version("0.1.2", md5="fced4160036e95fbbef3e7caafd47320")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-netstat", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-rselenium@1.7.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
