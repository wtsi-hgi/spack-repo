# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRidigbio(RPackage):
	"""Interface to the iDigBio Data API

	An interface to iDigBio's search API that allows downloading
  specimen records. Searches are returned as a data.frame. Other functions
  such as the metadata end points return lists of information. iDigBio is a US
  project focused on digitizing and serving museum specimen collections on the
  web. See <https://www.idigbio.org> for information on iDigBio.
	"""
	
	homepage = "https://github.com/iDigBio/ridigbio"
	cran = "ridigbio" 

	version("0.3.8", md5="a1ad1c53846ceae33ac20151829bea8a")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
