# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopendata(RPackage):
	"""Query and Download 'Rapid7' 'Cybersecurity' Data Sets

	'Rapid7' collects 'cybersecurity' data and makes it available via
    their 'Open Data' <http://opendata.rapid7.com> portal which has an API. Tools are
    provided to assist in querying for available data sets and downloading any
    data set authorized to a free, registered account.
	"""
	
	homepage = "https://github.com/brudis-r7/ropendata"
	cran = "ropendata" 

	version("0.1.0", md5="568c749dff04c592c685fb5e003436e2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
