# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSofa(RPackage):
	"""Connector to 'CouchDB'

	Provides an interface to the 'NoSQL' database 'CouchDB'
    (<http://couchdb.apache.org>). Methods are provided for managing
    databases within 'CouchDB', including creating/deleting/updating/transferring,
    and managing documents within databases. One can connect with a local
    'CouchDB' instance, or a remote 'CouchDB' databases such as 'Cloudant'. 
    Documents can be inserted directly from vectors, lists, data.frames, 
    and 'JSON'. Targeted at 'CouchDB' v2 or greater.
	"""
	
	homepage = "https://github.com/ropensci/sofa"
	cran = "sofa" 

	version("0.4.0", md5="651a838ad13ceff3e72395f36ae940df")

	depends_on("r-crul@0.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-r6@2.2.2:", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
