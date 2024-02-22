# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpushbullet(RPackage):
	"""R Interface to the Pushbullet Messaging Service

	An R interface to the Pushbullet messaging service which
 provides fast and efficient notifications (and file transfer) between
 computers, phones and tablets.  An account has to be registered at the 
 site <https://www.pushbullet.com> site to obtain a (free) API key.
	"""
	
	cran = "RPushbullet" 

	version("0.3.4", md5="7c7ca0162cc0444be64150bade019b4d")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
