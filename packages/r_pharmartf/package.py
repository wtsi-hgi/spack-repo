# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmartf(RPackage):
	"""Enhanced RTF Wrapper for Use with Existing Table Packages

	Enhanced RTF wrapper written in R for use with existing R tables
    packages such as 'Huxtable' or 'GT'. This package fills a gap where tables in
    certain packages can be written out to RTF, but cannot add certain metadata
    or features to the document that are required/expected in a report for a
    regulatory submission, such as multiple levels of titles and footnotes,
    making the document landscape, and controlling properties such as margins.
	"""
	
	cran = "pharmaRTF" 

	version("0.1.4", md5="5ec5bb469ec6928598a14edbe5419f22")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-huxtable@4.7.1:", type=("build", "run"))
