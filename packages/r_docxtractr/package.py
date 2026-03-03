# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocxtractr(RPackage):
	"""Extract Data Tables and Comments from 'Microsoft' 'Word'
Documents

	'Microsoft Word' 'docx' files provide an 'XML' structure that is fairly
    straightforward to navigate, especially when it applies to 'Word' tables and
    comments. Tools are provided to determine table count/structure, comment count
    and also to extract/clean tables and comments from 'Microsoft Word' 'docx' documents.
    There is also nascent support for '.doc' and '.pptx' files.
	"""
	
	homepage = "http://gitlab.com/hrbrmstr/docxtractr"
	cran = "docxtractr" 

	version("0.6.5", md5="3db9610b66a6996bd9066cb4661ec5ea")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
