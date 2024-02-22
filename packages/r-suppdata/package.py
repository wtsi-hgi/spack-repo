# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuppdata(RPackage):
	"""Downloading Supplementary Data from Published Manuscripts

	Downloads data supplementary materials from manuscripts,
    using papers' DOIs as references. Facilitates open, reproducible
    research workflows: scientists re-analyzing published datasets can
    work with them as easily as if they were stored on their own
    computer, and others can track their analysis workflow
    painlessly. The main function suppdata() returns a (temporary)
    location on the user's computer where the file is stored, making
    it simple to use suppdata() with standard functions like
    read.csv().
	"""
	
	homepage = "https://docs.ropensci.org/suppdata/"
	cran = "suppdata" 

	version("1.1-9", md5="36c59652796d03c0df3e3a8b016e5a81")

	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-xml2@1.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-rcrossref@0.8:", type=("build", "run"))
